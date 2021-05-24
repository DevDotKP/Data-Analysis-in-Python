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
