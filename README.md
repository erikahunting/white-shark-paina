## White Shark Pa'ina Project

Using data from recovered PSAT tags and estimated 
geolocation from individuals of the North Eastern Pacific 
white shark population, this script analyzes the diving 
behavior of individuals from the North Eastern Pacific 
White Shark poulation that visited the lee of Hawai'i 
island between 2000-2020 during their annual offshore 
migration and stayed for ~3 months. Using statistical
analysis and time series techniques, it searches for 
predicatable dive patterns from high-resolution archival
tag data.

## Getting Started
### Requirements
- [Python 3.10](https://www.python.org) or later
- [Jupyter Notebooks](https://jupyter.org)
- [Pandas 14.3](https://pandas.pydata.org) or later
- [Astral V2.2](https://astral.readthedocs.io/en/latest/) or later
- [Seaborn 0.11.2](https://seaborn.pydata.org) or later
- [Matplotlib 3.5](https://matplotlib.org) or later
- [NumPy 1.23.0](https://numpy.org) or later
- [Swifter 1.3.3](https://pypi.org/project/swifter/) or later
- [Pytz](http://pytz.sourceforge.net)
### Installation
#### Python
Install the latest version of Python for your operating 
system [here](https://www.python.org/downloads/release/python-3105/).

#### Anaconda, NumPy, and Pandas
Pandas has many dependencies that are may be time-comsuming
to keep track of. Thus, installing pandas and the rest of 
the [NumPy](https://numpy.org/) and [SciPy](https://scipy.org/) 
stack can be a little difficult for inexperienced users.

The simplest way to install not only pandas, but Python and 
the most popular packages that make up the SciPy stack 
([Jupyter Notebook](https://jupyter.org), [NumPy](https://numpy.org/), 
[Matplotlib](https://matplotlib.org/), …) is with [Anaconda](https://docs.continuum.io/anaconda/), 
a cross-platform (Linux, macOS, Windows) Python distribution 
for data analytics and scientific computing.

After running the installer, the user will have access to 
pandas and the rest of the SciPy stack without needing to 
install anything else, and without needing to wait for any 
software to be compiled.

Installation instructions for Anaconda can be found [here](https://docs.continuum.io/anaconda/install/).

A full list of the packages available as part of the 
Anaconda distribution can be found [here](https://docs.continuum.io/anaconda/packages/pkg-docs/).

Another advantage to installing Anaconda is that you don’t 
need admin rights to install it. Anaconda can install in 
the user’s home directory, which makes it trivial to delete 
Anaconda if you decide (just delete that folder).

If you do not wish to use Anaconda (though it is strongly 
recommended), you can install Pandas using Miniconda or 
PyPI. Details and dependencies be found [here](https://pandas.pydata.org/docs/getting_started/install.html).

#### Jupyter Notebook
If you have downloaded Anaconda, Jupyter Notebook has 
already been installed. If you are not using Anaconda, 
install the classic Jupyter Notebook by running:
```````
[pip install notebook]
```````
in your terminal or other command-line shell.

To run the notebook:
```````
[jupyter notebook]
```````

#### Matplotlib and Seaborn
Seaborn is a Python data visualization library based on 
matplotlib. It provides a high-level interface for drawing 
attractive and informative statistical graphics. If you 
have not downloaded Anaconda (which has installed Matplotlib
for you), Matplotlib releases are available as wheel packages 
for macOS, Windows and Linux on [PyPI](https://pypi.org/project/matplotlib/). Install it using pip:
```````
[python -m pip install -U pip]
[python -m pip install -U matplotlib]
```````
If this command results in Matplotlib being compiled from 
source and there's trouble with the compilation, you can add
```````
[--prefer-binary]
```````
to select the newest version of Matplotlib for which there 
is a precompiled wheel for your OS and Python.

Official releases of seaborn can then be installed from [PyPI](https://pypi.org/project/seaborn/):
```````
[pip install seaborn]
```````
The library is also included as part of the Anaconda distribution:
```````
[conda install seaborn]
```````

#### Astral V2.2 and pytz
Astral is a python package for calculating the times of 
various aspects of the sun and phases of the moon. 
Install Astral V2.2:
```````
[pip install astral]
```````
Pytz is a Python package for world timezone definitions, 
modern and historical. Install the latest version of pytz:
```````
[pip install pytz]
```````
## Options
#### Swifter
Swifter is not necessary, but highly recommended. It is a 
package which efficiently applies any function to a pandas 
dataframe or series in the fastest available manner and 
will dramatically decrease code runtime.
To install the latest version of swifter:
```````
[pip install swifter]
```````
## Resources
### Articles, Tutorials, ect.
- [Set up Virtual Environemnt for Python Using Anaconda](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/?ref=lbp)
- [Advantages of Python Pandas](https://data-flair.training/blogs/advantages-of-python-pandas/)
- [Python vs. R for Data Science](https://towardsdatascience.com/python-vs-r-for-data-science-cf2699dfff4b)
- [Parallelizing your code](https://stackoverflow.com/questions/45545110/make-pandas-dataframe-apply-use-all-cores)
- [List of Timezones available in pytz](https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones)
### Support
[ehunting@stanford.edu](ehunting@stanford.edu)
### Contributing and Contact
[ehunting@stanford.edu](ehunting@stanford.edu)

[Stanford Block Lab](https://www.stanfordblocklab.org)
