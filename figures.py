import datetime as dt
import pytz
import matplotlib.pyplot as plt
import numpy as np
import os

from os import listdir
from os.path import isfile, join

import pandas as pd
import re
import seaborn as sns
import sys


# Written by Erika Hunting ehunting@stanford.edu for 
# plotting archival White Shark tag Data for 2022
# Stanford@SEA White Shark Pa'ina project


# processing data #########################################
def convertUtcToHi(hour):
    """
    Given an hour in 24 hour clock in UTC, converts to
    local time Hawaii
    """
    
    if hour >= 10:
        return hour - 10
    return 24 - (10 - hour)

def getStandardizedDatetime(row, originaltzstring):
    originaltz = pytz.timezone(originaltzstring)
    originaldt = dt.datetime(row["Year"], row["Month"], row["Day"], row["Hour"], row["Min"], row["Sec"], 0, originaltz)
    return originaldt.astimezone(pytz.timezone("Pacific/Honolulu"))
    
def getTimeOfDay(hour):

    # call api later
    sunrise = 6
    sunset = 18
    
    if hour in range(sunrise + 1, sunset - 1):
        return 'Day'
    elif hour in range(sunset + 1, 24) or hour in range(0, sunrise - 1):
        return 'Night'
    elif hour in range(sunrise - 1, sunrise + 1):
        return 'Dawn'
    else:
        return 'Dusk'


def getPlotData(filename):
    """
    Given a filename to corrected archival White Shark tag
    data, returns a pandas dataframe containing data for
    plotting
    """
    df = pd.read_csv(filename)
    
    # Get timezone of date/time
    dateColName = df.columns[0]
    originaltz = ''
    if dateColName == "Date(UTC-8)":
        originaltz = 'Etc/GMT+8' # why? no one knows
    elif dateColName == "Date(EST)":
        originaltz = 'UTC' # Why? EST was mistake
    elif dateColName == "Date":
        originaltz = 'UTC'
    else:
        raise ValueError("Cannot processes timezone of Date column" + dateColName)
    
    # Build standard datetime
    df["Datetime (UTC-10)"] = df.apply(lambda row: getStandardizedDatetime(row, originaltz), axis=1)
    
    # add hour column
    df["Hour (UTC-10)"] = df["Datetime (UTC-10)"].apply(lambda x: x.hour)
    
    # add time of day
    df["Time of Day"] = df["Hour (UTC-10)"].apply(getTimeOfDay)
    
    return df


def resample(df, sampleRate):
    """
    Given a pandas dataframe and a sample rate, resamples
    data at given sample rate.
    """

    #date MM/DD/YYYY
    dates = list(df["Date"])
    
    #time string HH:MM:SS
    times = list(df["Time"])

    # depth, expressed in meters (m) to the tenths place
    depths = list(df["Depth(m)"])
    
    # hour of the day (0-24)
    hours = list(df["Hour"])
    
    resampledDates = []
    resampledTimes = []
    resampledDepths = []
    resampledHours = []
    
    i = 0
    while i < len(times):
        resampledDates.append(dates[i])
        resampledTimes.append(times[i])
        resampledDepths.append(depths[i])
        resampledHours.append(hours[i])
        i += sampleRate
    
    d = {
        'Date': resampledDates,
        'Time': resampledTimes,
        'Depth(m)': resampledDepths,
        'Hour': resampledHours,
        }
        
    return pd.DataFrame(d)


# plotting data ###########################################
def plotDepthTimeScatter(pdArchivalData, Id):
    """
    Given a pandas dataframe of corrected archival white
    shark tag data and a string of the sharks's ID, plots a
    scatter plot of depth vs time.
    """
    
    y = "Depth(m)"
    sns.set_theme()
    g = sns.relplot(data=pdArchivalData,
                x="Time",
                y=y,
                label='Depth (m)')
    
    g.fig.autofmt_xdate()
    g.fig.suptitle('Depth vs. Time for ' + Id)
    

def plotDepthTimeViolin(pdArchivalData, numDays, Id):
    """
    Given a pandas dataframe of corrected archival white
    shark tag data, the number of days from the start of
    the data, and a string of the shark's ID, plots a
    violin plot of depth vs time with days on the x axis
    and daytime and nightime depth represented by the
    distributions for numDays.
    """
    isDay = listDayNight(list(pdArchivalData["Hour"]))
    
    # just plot a week's worth of data
    dates = list(pdArchivalData["Date"])
    seenDates = []
    
    i = 0
    while len(seenDates) < numDays:
        date = dates[i]
        if not date in seenDates:
            seenDates.append(date)
        i += 1
    
    # convert to pandas dataframe
    d = {
        'Date': dates[:i],
        'Depth(m)': list(pdArchivalData["Depth(m)"])[:i],
        'Time of Day': isDay[:i]
        }
    df = pd.DataFrame(d)
            
    # Apply the default theme
    sns.set_theme()
    
    g = sns.catplot(data=df, kind="violin", x="Date", y="Depth(m)", hue="Time of Day", split=True)
    g.fig.autofmt_xdate()
    g.fig.suptitle('Depth vs. Time for ' + Id)
    
    
def plotDepthTimeViolinHours(pdArchivalData, Id):
    """
    Given a pandas dataframe of corrected archival white
    shark tag data, the number of days from the start of
    the data, and a string of the shark's ID, plots a
    violin plot of depth vs time with hours on the x axis
    for numDays.
    """
    isDay = listDayNight(list(pdArchivalData["Hour"]))

    dates = list(pdArchivalData["Date"])

    #time string HH:MM:SS
    times = list(pdArchivalData["Time"])
    
    # convert to pandas dataframe
    d = {
        'Date': dates,
        'Depth(m)': list(pdArchivalData["Depth(m)"]),
        'Hour': list(pdArchivalData["Hour"]),
        'Time of Day': isDay
        }
    df = pd.DataFrame(d)
            
    # Apply the default theme
    sns.set_theme()
    
    g = sns.catplot(data=df, kind="violin", x="Hour", y="Depth(m)", hue="Time of Day", split=False)
    
    g.fig.autofmt_xdate()
    g.fig.suptitle('Depth vs. Time for ' + Id)
    
    
def plotHeatMap(pdArchivalData, Id):
    """
    """
    
    # Apply the default theme
    sns.set_theme()
   
    binSize = 10
    maxDepth = 700
    bins = np.arange(0, maxDepth, binSize)
    pdArchivalData["Depth Bin"] = pd.cut(pdArchivalData["Depth(m)"], bins=bins, labels=bins[:-1])
#    print(pdArchivalData.head(20))
    
    grouped = pdArchivalData.groupby(["Hour (UTC-10)", "Depth Bin"]).size().reset_index(name='count')
#    print(grouped.head(20))
    piv = grouped.pivot("Depth Bin", "Hour (UTC-10)", "count")
#    print(piv.head(10))
    
    ax = sns.heatmap(piv)
    
    ## normalize column by dividing by num rows
    ## rename depth bin y axis
    
def plotDepthDuration(pdArchivalData, Id):
    """
    """
    
    # Apply the default theme
    sns.set_theme()
    ##piv = grouped.pivot("Depth Bin", "count")
    #print('PIV', piv.head())
#    print(grouped.head(20))
#    print('DTYEP', grouped.dtypes)
    
    ax = sns.histplot(pdArchivalData, x="Depth(m)", hue="Time of Day", stat="density", common_norm=False) # kind="kde", fill=True) #hue="sex", kind="kde", fill=True)
    ax.set_xlim(0, 700)
#    ax.invert_xaxis()
    
    
    ## filter diving hours around sunset / sunrise
    # compare just day and night
    

def printQuickStats(pdArchivalData, Id):
    """
    Given a pandas dataframe of corrected archival white
    shark tag data and a string of the shark ID, returns
    the average depth during the day and average depth
    during the night. Day is defined as 6a-6p Hawaii time.
    """
    
    depths = list(pdArchivalData["Depth(m)"])
    isDay = listDayNight(list(pdArchivalData["Hour"]))
    dayDepths = []
    nightDepths = []
    
    for i in range(len(isDay)):
        if isDay[i] == 'day':
            dayDepths.append(depths[i])
        else: # night
            nightDepths.append(depths[i])
    
    print('Quick stats for ', Id,
    'Daytime \n average depth: ', average(dayDepths),
    '\n', 'standard deviation: ',
    np.std(np.array(dayDepths)), '\n'
    'Night time \n average depth: ', average(nightDepths),
    '\n', 'standard deviation: ',
    np.std(np.array(nightDepths)))


def listDayNight(hours):
    """
    Given a list of daytime hours, returns a list of
    strings of the same length classifing each time as
    'day' or 'night'.
    """
    isDay = []
    
    # call api later to get sunset and sunrise but
    # for now say 6pm - 6am is night
    for i in range(len(hours)):
        hour = hours[i]
        if hour < 18 and hour > 6:
            isDay.append('day')
        else: # night
            isDay.append('night')
    
    return isDay
    
    
def average(lst):
    """
    Given a list of int, returns the average.
    """
    return sum(lst) / len(lst)
    
def std(lst):
    """
    Given a list of int, returns the standard deviation.
    """
    
    return np.std(np.array(lst))
    

if __name__ == "__main__":

    # enter name of dir_path to make figures for e.g.
    # Erika@erikas-mbp python3.8 figures.py dir_path
    
    filename = sys.argv[1]
    
    df = getPlotData(filename)
#    print(pdArchivalDepthData.dtypes)
#    print(pdArchivalDepthData)
#    plotDepthTimeScatter(resample(pdArchivalDepthData, 50), filename)
#    print(df.info())
#    print(len(df[df["Depth(m)"] == 0]))
    plotHeatMap(df, filename)


    # do regex for shark ID later
    
    # would be interesting to look at nautical almanac for moon cycles
    # there seems to be a monthly periodicity
#    plotDepthTimeViolin(pdArchivalDepthData, 28, filename) #filename = ID
#    plotDepthTimeViolinHours(pdArchivalDepthData, filename) #filename
#    printQuickStats(pdArchivalDepthData, filename)
    
#    plotDepthDuration(df, filename)

    plt.show()
