import matplotlib.pyplot as plt
import pandas as pd
import requests

import Constants  # Using the defined constants

url = Constants.STARBUCKS

r = requests.get ( url=url, headers=Constants.HEADER )
starbucksDF = pd.read_html ( r.text, index_col='Date',
                             parse_dates=True )  # With 'parse_dates=True', we are informing Python/Pandas that the index column has DateTime values
starbucksDF = starbucksDF[0]
starbucksDF = starbucksDF.drop ( 'Unnamed: 0',
                                 axis=1 )  # Removing the unnamed:0 column. It should normally not appear after you define an index column, like we've done, but was not removed in this case. Warrants a research on the issue

# https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/01-Time-Resampling.ipynb can be used to check for more frequencies

print ( starbucksDF.resample ( rule='A' ).mean () )  # Converting business week data to yearly data

ax = starbucksDF['Close'].resample ( 'A' ).mean ().plot.bar ( title='Average mean closing price',
                                                              grid=True )  # Shows the average closing price AT THE END of each year
ax.set ( xlabel='Year', ylabel=Constants.USD )
plt.show ()

title = 'Max monthly closing price for SBUX'
ax = starbucksDF['Close'].resample ( rule='M' ).max ().plot.line ( color=(0.52, 0.32, 0.31), title=title,
                                                                   grid=True )  # Giving color values from (r,g,b) that range from [0,1]
ax.set ( xlabel='Month', ylabel=Constants.USD )
plt.show ()

# Rolling averages
starbucksDF['Close'].plot ( figsize=(12, 5) )
starbucksDF.rolling ( window=30 ).mean ()['Close'].plot ( grid=True, color=(.26, .12, .53) )
plt.show ()

# Tip: If you do not give plt.show() after each SIMILAR graph, they will appear on the same graph

# What is expanding average?
# A common alternative to rolling statistics is to use an expanding window, which yields the value of the statistic with all the data available up to that point in time.

ax = starbucksDF['Close'].expanding ().mean ().plot ( title='Expanding average', color=(.12, .98, .43), grid=True )
ax.set ( xlabel='Time', ylabel=Constants.USD )
plt.show ()
