import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv (
    r'C:\Users\kisho\Desktop\Programming\Learning\Data analysis with Python\UDEMY_TSA_FINAL\03-Pandas-Visualization\df1.csv',
    index_col=0 )  # index_col is used to define the index column for the data. Here, column 0 is the index
print ( df1.head () )

df2 = pd.read_csv (
    r'C:\Users\kisho\Desktop\Programming\Learning\Data analysis with Python\UDEMY_TSA_FINAL\03-Pandas-Visualization\df2.csv' )
print ( df2.head () )

# Plotting a histogram ( For continous data)
print ( '\nHistogram\n' )
df1['A'].plot.hist ()
plt.show ()  # Required for the plot to show up in PyCharm

# We can also demarcate the bars with an edge colour; The naming convention can be found here = https://matplotlib.org/stable/gallery/color/named_colors.html
print ( '\nHistogram with bars edges marked\n' )
df1['A'].plot.hist ( edgecolor='firebrick', bins=50, grid=True ).autoscale ( enable=True, axis='both',
                                                                             tight=True )  # Bins mean the number of bars for a particular set of data
# Grid = True does what it says, makes grids in the plot for better understanding
plt.show ()

# Plotting a bar plot ( For discrete data)
print ( '\nBar chart' )
df2.plot.bar ()  # Compares the value of columns a,b,c and d at each index column as separate bars
plt.show ()
df2.plot.bar ( stacked=True,
               grid=True )  # Compares the value of columns a,b,c and d at each index column as a single bar per index
plt.show ()
df2.plot.barh ( stacked=True, grid=True )  # Shows the bar horizontally instead of vertically
plt.show ()

# Plotting a line chart
print ( '\nLine chart\n' )
df2.plot.line ( y='a' )  # The Y axis has to be defined. The X axis is the index
plt.show ()

df2.plot.line ( y=['a', 'b', 'c'], figsize=(10, 4) )  # The Y axis has to be defined. The X axis is the index
plt.show ()

# Plotting an area chart
print ( '\nArea chart\n' )
df2.plot.area ()
plt.show ()

# Plotting an scatter chart
print ( '\nScatter chart\n' )
df1.plot.scatter ( x='A', y='B' )
plt.show ()

# Plotting a box plot
print ( '\nBox plot\n' )
df2.boxplot ()
plt.show ()

# Plotting a hexagonal bin plot
print ( '\nBox plot\n' )
df2.boxplot ()
plt.show ()

# Plotting a hexagonal bin distribution chart
print ( '\nHexagonal bin distribution\n' )
df = pd.DataFrame ( data=(np.random.randn ( 1000, 2 )), columns=['a', 'b'] )
print ( df )
df.plot.hexbin ( x='a', y='b', gridsize=40 )
plt.show ()
