import matplotlib.pyplot as plt
import pandas  as pd

import Constants

milkProdDF = pd.read_html ( Constants.readhtml ( Constants.MILK_PRODUCTION ).text )
milkProdDF = milkProdDF[0]
milkProdDF = milkProdDF.drop ( 'Unnamed: 0', axis=1 )

# What is the current data type of the Date column?
print ( '\nA1: ', milkProdDF['Date'].dtypes )

# Change the Date column to a datetime format
milkProdDF['Date'] = pd.to_datetime ( milkProdDF['Date'] )
print ( '\nA2: ', milkProdDF['Date'].dtypes )

# Set the Date column to be the index column
milkProdDF = milkProdDF.set_index ( 'Date' )
print ( '\nA3: \n', milkProdDF.head ( 2 ) )

# Plot the DF with a line plot
ax = milkProdDF.plot ( grid=True, title=' A4 : Milk Production vs Time', color=(.51, .12, .01) )
ax.set ( xlabel=Constants.TIME, ylabel=Constants.PRODUCTION )
print ( '\nA4: \n' )
plt.show ()

# Add a column called month that takes the value of the month.
milkProdDF['Month'] = milkProdDF.index.month
print ( milkProdDF )
print ( '\nA5: \n', milkProdDF )

# Get the name of the month instead of the value
milkProdDF['Month'] = milkProdDF.index.strftime ( '%B' )
print ( '\nA6: \n', milkProdDF )

# Draw a box plot that groups data ny month
milkProdDF.boxplot ( by='Month', figsize=(12, 5) )
plt.show ()
