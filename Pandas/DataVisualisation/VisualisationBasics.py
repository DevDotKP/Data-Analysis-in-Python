import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv (
    r'C:\Users\kisho\Desktop\Programming\Learning\Data analysis with Python\UDEMY_TSA_FINAL\03-Pandas-Visualization\df1.csv',
    index_col=0 )  # index_col is used to define the index column for the data. Here, column 0 is the index
print ( df1.head () )

df2 = pd.read_csv (
    r'C:\Users\kisho\Desktop\Programming\Learning\Data analysis with Python\UDEMY_TSA_FINAL\03-Pandas-Visualization\df2.csv' )
print ( df2.head () )

# Plotting a histogram
print ( '\nHistogram\n' )
df1['A'].plot.hist ()
plt.show ()  # Required to show up in PyCharm
