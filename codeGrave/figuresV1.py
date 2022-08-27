from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

import re

import seaborn as sns
import sys




#from os import listdir
#from os.path import isfile, join


# Written by Erika Hunting ehunting@stanford.edu for 
# plotting archival White Shark tag Data for 2022
# Stanford@SEA White Shark Pa'ina project


# processing data #########################################
def getPlotData(filename):
    """
    Given a filename to corrected archival White Shark tag
    data, returns a pandas dataframe containing data for
    plotting
    """
    
#    df = pd.read_csv(filename)
#
#    # date string MM/DD/YYYY
#    dates = list(df["Date"])
#
#    # time string HH:MM:SS
#    times = list(df["Time"])
#
#    # depth, expressed in meters (m) to the tenths place
#    depths = list(df["Depth(m)"])
    
    
    
#    data = np.genfromtxt(filename, delimiter=',')
#    print('data: ', data)
    
    # date MM/DD/YYYY
#    dates = df[:, 0]
#    print('dates: ', dates, 'type: ', type(dates[0]))
#
#    # UTC time stamp HH:MM:SS
#    times = df[:, 1]
#
#    # depth, expressed in meters (m) to the tenths place
#    depths = df[:, 2]
    
#    # convert to pandas dataframe
#    d = {
#        'Date (MM/DD/YYYY)': dates,
#        'Time (HH:MM:SS)': times,
#        'Depth (m)': depths,
#        }
#    pdArchivalData = pd.DataFrame(d)

#    # convert unix timestamp to normal date time
#    pdUserData['Date'] = pd.to_datetime(pdUserData['Date'],unit='ms')

    return pd.read_csv(filename)

def resample(df, sampleRate):
    """
    Given a pandas dataframe and a sample rate, resamples data
    at given sample rate.
    """
    print('HERE', df[0:0], '\n')
    print('COLUMNS', df.columns, '\n')
    print('COLUMNS 0', df.columns[0], '\n')
    
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
    
    # convert to pandas dataframe
    d = {
        'Date': resampledDates,
        'Time': resampledTimes,
        'Depth(m)': resampledDepths,
        'Hour': resampledHours,
        }
    return pd.DataFrame(d)
    
    


#def getMetadata(filename):
#    """
#    Given a filepath to Tejas's metadata, return dict of
#    Id as keys and values as covid positive dates or Nan
#    if user with that Id never tested positive.
#    """
#        data = np.genfromtxt(filename, delimiter=',')
#
#    # ID of the white shark
#    Ids = subset[:, 0]
#
#    # tag number
#    tagNums = subset[:, 1]
#
#    # ppt
#    ppts = subset[:, 2]
#
#    # date tagged
#    taggingDates =  subset[:, 3]
#
#    # sex (M or F)
#    sexs = subset[:, 4]
#
#    # latitude of event, expressed in degrees
#    lats = subset[:, 5]
#
#    # longitude of event, expressed in degrees
#    longs = ubset[:, 6]
    
    # date of event
    
    
#    data = pd.read_csv(filename)
#
#    justPositives = data.dropna(axis=0)
#
#    Ids = list(justPositives['qr_code_scan'])
#
#    # if participant ever tested positive, their date will
#    # be here. If they never tested positive, this value
#    # will be Nan. If they were positive for multiple
#    # days, then the value will be a list containing start
#    # and end date for postive.
#    positivePeriods = list(justPositives['covid_date'])
#    positivePeriods2 = [str(period) for period in positivePeriods]
#
#    positivePeriods3 = []
#    for period in positivePeriods2:
#
#        if ';' in period:
#            nestedDateList = []
#            allDates = period.split(';')
#
#            startDate = allDates[0]
#            endDate = allDates[-1]
#
#            # convert to datetime
#            startDate2 = pd.to_datetime(startDate, format='%m/%d/%Y')
#            if endDate == '':
#                endDate2 = startDate2 + timedelta(hours=24)
#            else:
#                endDate2 = (pd.to_datetime(endDate, format='%m/%d/%Y')
#                    + timedelta(hours=24))
#
#            nestedDateList.append(startDate2)
#            nestedDateList.append(endDate2)
#            positivePeriods3.append(nestedDateList)
#
#        else:
#            date = pd.to_datetime(period, format='%m/%d/%Y')
#            positivePeriods3.append(date)
#
#    IdsToPeriods = {}
#    for i in range(len(Ids)):
#        Id = Ids[i]
#        positivePeriod = positivePeriods3[i]
#        IdsToPeriods[Id] = positivePeriod
#
#    return IdsToPeriods


# plotting data ###########################################
def plotDepthTimeScatter(pdArchivalData, Id):
    """
    Given a pandas dataframe of corrected archival white
    shark tag data and a string of the sharks's ID, plots a
    scatter plot of depth vs time.
    """
    # data = pdArchivalData
    y = "Depth(m)"
    
    # Apply the default theme
    sns.set_theme()
    
    # Create a visualization
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
    
    isDay = []
    
    
    # if between sunset and sunrise - night
    
    # call api later to get sunset and sunrise but
    # for now say 6pm - 6am is night
    hours = list(pdArchivalData["Hour"])
    
    for i in range(len(hours)):
        hour = hours[i]
        # call api later to get sunset and sunrise but
        # for now say 6pm - 6am is night
        
        # wierd skewing could be due to not picking
        # right times for night and day shoal
        
        # try making night between 7p and 5a
        # shark feeding patterns match this ?
        
        if hour < 18 and hour > 6:
            isDay.append('day')
        else: # night
            isDay.append('night')
#    print(isDay)
    
    # check
#    valCounts = {}
#    for val in isDay:
#        if not val in valCounts.keys():
#            valCounts[val] = 0
#        valCounts[val] += 1
#    print(valCounts)
    
    # convert to pandas dataframe for plotting
    # depth, expressed in meters (m) to the tenths place
    
    
    # just plot a week's worth
    seenDates = []
    dates = list(pdArchivalData["Date"])
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
    
    isDay = []
    
    
    # if between sunset and sunrise - night
    
    # call api later to get sunset and sunrise but
    # for now say 6pm - 6am is night
    hours = list(pdArchivalData["Hour"])
    
    for i in range(len(hours)):
        hour = hours[i]
        # call api later to get sunset and sunrise but
        # for now say 6pm - 6am is night
        
        # wierd skewing could be due to not picking
        # right times for night and day shoal
        
        # try making night between 7p and 5a
        # shark feeding patterns match this ?
        
        if hour < 18 and hour > 6:
            isDay.append('day')
        else: # night
            isDay.append('night')
#    print(isDay)
    
    # check
#    valCounts = {}
#    for val in isDay:
#        if not val in valCounts.keys():
#            valCounts[val] = 0
#        valCounts[val] += 1
#    print(valCounts)
    
    # convert to pandas dataframe for plotting
    # depth, expressed in meters (m) to the tenths place
    
    
    # just plot a week's worth
#    seenDates = []
#    dates = list(pdArchivalData["Date"])
#    i = 0
#    while len(seenDates) < numDays:
#        date = dates[i]
#        if not date in seenDates:
#            seenDates.append(date)
#        i += 1
    
    
    # convert to pandas dataframe
    d = {
        'Date': list(pdArchivalData["Date"]), #[:i],
        'Depth(m)': list(pdArchivalData["Depth(m)"]), #[:i],
        'Hour': list(pdArchivalData["Hour"]),
        'Time of Day': isDay #[:i]
        }
    df = pd.DataFrame(d)
            
    # Apply the default theme
    sns.set_theme()
    
    g = sns.catplot(data=df, kind="violin", x="Hour", y="Depth(m)", hue="Time of Day", split=False)
    
    g.fig.autofmt_xdate()
    g.fig.suptitle('Depth vs. Time for ' + Id)
    
#def findHourAverages


#def plotHr(pdUserData, participantId, positivePeriod):
#    """
#    Given a pandas dataframe of user data and a string of
#    the user's QR-code ID and positive period, plots a
#    graph of the indicated metric vs time.
#    """
#    data = pdUserData
#    y = "Heart Rate (bpm)"
#    g = sns.relplot(x="Date",
#                    y=y,
#                    kind="line",
#                    data=data,
#                    color='red',
#                    linewidth=0.5,
#                    label='Heart Rate (bpm) COVID-19 Negative')
#    g.fig.autofmt_xdate()
#    if positivePeriod is not False:
#        highlightPositiveDates(data, y, positivePeriod)
#    g.fig.suptitle('Heart Rate vs. Time for ' + participantId)
#
#
#def plotEda(pdUserData, participantId, positivePeriod):
#    """
#    Given a pandas dataframe of user data and a string of
#    the user's QR-code ID and positive period, plots a
#    graph of the indicated metric vs time.
#    """
#    data = pdUserData
#    y = "EDA (μS)"
#    g = sns.relplot(x="Date",
#                    y=y,
#                    kind="line",
#                    data=data,
#                    color='purple',
#                    linewidth=0.5,
#                    label='EDA (μS) COVID-19 Negative')
#    g.fig.autofmt_xdate()
#    if positivePeriod is not False:
#        highlightPositiveDates(data, y, positivePeriod)
#    g.fig.suptitle('EDA Measurement vs. Time for ' + participantId)


#def highlightPositiveDates(df, y, positivePeriod):
#    """
#    Given a string y indicating which measurement
#    to graph e.g. 'Skin Temperature (°C)' and a
#    pd dataframe of user data, highlight the dates
#    during which a participant was positive.
#    """
#    startDate =  positivePeriod[0]
#    endDate = positivePeriod[-1]
#
#    # plot subset on top of the normal time series
#    sns.lineplot(
#        x="Date",
#        y=y,
#        data=df[(df['Date'] > startDate) & (df['Date'] < endDate)],
#        color='green',
#        legend='brief',
#        label= y + ' COVID-19 Positive'
#        )

# def graphs():
#     """
#     Plots all three graphs for all users in a directory!
#     """
#     IdsToPeriods = getMetadata(metadata)
#     # change directory if you are not working on Erika's computer!
#     directory = r'/Users/Erika/Desktop/STN_data'
#     for filename in os.listdir(directory):
#         if filename.endswith(".csv"):
#             participantId = filename[0: -4]
#             data = getDataToPlot(filename)
#             positivePeriod = IdsToPeriods[participantId]
#             #plotTemp(data, participantId, positivePeriod)
#             #plotHr(data, participantId, positivePeriod)
#             plotEda(data, participantId, positivePeriod)
#             plt.show()
#         else:
#             continue

# smooth data ? not really important if just taking avg over sick period

#put on pdf? maybe build this out if specified by an argument


if __name__ == "__main__":

    
    # enter name of file to run report on e.g.
    # Erika@erikas-mbp STN_data % python3.8 figures.py data.csv meta.csv
    
    
    
    
    
    filename = sys.argv[1]
    pdArchivalDepthData = getPlotData(filename)
    print(pdArchivalDepthData)
    
    # Mia change second parameter in resample function to sample every num
    # times e.g. ... resample (..., 200) plots every 200 samples
    plotDepthTimeScatter(resample(pdArchivalDepthData, 100), filename)
    
    
    # would be interesting to look at nautical almanac for moon cycles
    # there seems to be a monthly periodicity
    plotDepthTimeViolin(pdArchivalDepthData, 28, filename)
    plotDepthTimeViolinHours(pdArchivalDepthData, filename)
    
    plt.show()
    
    # violin plt maybe days on x... day and night like in docs
    # distribution
    
    
    
    
    
    
    
    
    
#    # enter name of file to run report on e.g.
#    # Erika@erikas-mbp STN_data % python3.8 figures.py data.csv meta.csv
#
#    metadata = sys.argv[2]
#
#    IdsToPeriods = getMetadata(metadata)
#
#    # # show graphs for all files in the directory
#    # if sys.argv[1] == 'everyone':
#    #     graphs()
#
#    # else:
#        # if given a filename for a specific user (e.g.
#        # GP-028.csv), then only show graphs for this person
#        # will show
#    filename = sys.argv[1]
#    participantId = filename[0: -4]
#    if participantId in IdsToPeriods.keys():
#        positivePeriod = IdsToPeriods[participantId]
#    else:
#        positivePeriod = False
#
#    data = getDataToPlot(filename)
#    plotTemp(data, participantId, positivePeriod)
#    plotHr(data, participantId, positivePeriod)
#    plotEda(data, participantId, positivePeriod)
#    plt.show()
#
    
    # can turn each station csv into a pd dataframe, then concatinate them
    
    # can take average at one depth and do a scatter plot ?

    # use . where to get ties for depth vs time scatter
    # for each shark
    # find the centroid of depths
    # is this ok for the changing lat long? - probably
    # just use a regex on the filename to pull out the shark ID or just print first whatever nums
    # of the filename
