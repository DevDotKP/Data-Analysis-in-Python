import matplotlib.pyplot as plt
import pandas as pd
import requests

url = 'https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/starbucks.csv'

header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest"
}
r = requests.get ( url=url, headers=header )
starbucksDF = pd.read_html ( r.text, index_col='Date',
                             parse_dates=True )  # With 'parse_dates=True', we are informing Python/Pandas that the index column has DateTime values
starbucksDF = starbucksDF[0]
starbucksDF = starbucksDF.drop ( 'Unnamed: 0',
                                 axis=1 )  # Removing the unnamed:0 column. It should normally not appear after you define an index column, like we've done, but was not removed in this case. Warrants a research on the issue

# https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/01-Time-Resampling.ipynb can be used to check for more frequencies

print ( starbucksDF.resample ( rule='A' ).mean () )  # Converting business week data to yearly data

ax = starbucksDF['Close'].resample ( 'A' ).mean ().plot.bar ( title='Average mean closing price',
                                                              grid=True )  # Shows the average closing price AT THE END of each year
ax.set ( xlabel='Year', ylabel='USD $' )
plt.show ()

title = 'Max monthly closing price for SBUX'
ax = starbucksDF['Close'].resample ( rule='M' ).max ().plot.line ( color=(0.52, 0.32, 0.31), title=title,
                                                                   grid=True )  # Giving color values from (r,g,b) that range from [0,1]
ax.set ( xlabel='Month', ylabel='USD $' )
plt.show ()
