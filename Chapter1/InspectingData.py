# Chapter 1 | Module 3

import pandas as pd

df = pd.read_csv ( r'C:\Users\kisho\Desktop\Programming\astronauts.csv' )

print ( df.head ( 2 ) )  # Picks from the start of the data
print ( df.tail ( 3 ) )  # Picks from the end of the data
print ( df.sample ( 5 ) )  # Picks randomly

print ( df.info () )  # Provides information about the data types of the DataFrame

print ( df.describe () )  # Provides information about the data like mean, count, quartiles

print ( df.corr () )  # Provides the correlation of the data, learn it in statistics

print ( df['Year'].value_counts () )  # Provides the number of times each value was mentioned for the 'Year' column

print ( df.max () )  # Provides the maximum in each column; It is not necessarily from the same row

print ( df.median () )  # Provides the median in each column; It is not necessarily from the same row
