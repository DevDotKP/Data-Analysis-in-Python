import matplotlib.pyplot as  plt
import pandas as pd
from matplotlib import dates

import Constants

starbucksDF = pd.read_html ( Constants.readhtml ( Constants.STARBUCKS ).text, index_col='Date',
                             parse_dates=True )  # With 'parse_dates=True', we are informing Python/Pandas that the index column has DateTime values
starbucksDF = starbucksDF[0]
starbucksDF = starbucksDF.drop ( 'Unnamed: 0',
                                 axis=1 )  # Removing the unnamed:0 column. It should normally not appear after you define an index column, like we've done, but was not removed in this case. Warrants a research on the issue

# Limiting the axis', per requirement

# Two methods to achieve that, we can either filter the data out at the DF level, or the plot level

# DF level filtering
starbucksDF['Close']['2017-01-01' :'2017-12-31'].plot ( title='DF level filtering', figsize=(12, 5), ylim=[50, 70],
                                                        ls='--', color=(
        .312, .42, .21) )  # Give me information for only the year 2017
plt.show ()

# Plot level filtering
starbucksDF['Close'].plot ( title='Plot level filtering', xlim=['2017-01-01', '2017-12-31'], figsize=(12, 3),
                            ylim=[50, 70] )
plt.show ()

# Modifying x and y ticks
ax = starbucksDF['Close']['2017-01-10' :'2017-03-31'].plot ( title='X and Y ticks modification', ylim=[50, 70],
                                                             grid=True, color=(.41, .51, .51) )
ax.set ( xlabel=Constants.TIME, ylabel=Constants.USD )
## For Major axis
ax.xaxis.set_major_locator ( dates.MonthLocator ( bymonthday=28 ) )  # Shows the data by month for every 28 days.
# For reference, try:  https://matplotlib.org/stable/api/dates_api.html
ax.xaxis.set_major_formatter ( dates.DateFormatter (
    '%b-%Y' ) )  # For reference on these codes (%b, %Y), look up https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/Reference/TickReference.ipynb

## For minor axis
ax.xaxis.set_minor_locator ( dates.WeekdayLocator ( byweekday=0 ) )
ax.xaxis.set_minor_formatter ( dates.DateFormatter (
    '\n\n\n\n%d' ) )  # \n added so that at times of overlap, the major and minor axis do not write over each other
plt.show ()
