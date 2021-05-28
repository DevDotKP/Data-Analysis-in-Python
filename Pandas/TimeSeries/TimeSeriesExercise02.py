import pandas  as pd
from matplotlib import pyplot as plt
from matplotlib import ticker

import Constants

umtmvsDF = pd.read_html ( Constants.readhtml ( Constants.UMTMVS ).text, index_col='DATE', parse_dates=True )
umtmvsDF = umtmvsDF[0]
umtmvsDF = umtmvsDF.drop ( 'Unnamed: 0', axis=1 )

# What was the percentage decrease in value from Jan 2009 to Jan 2019?
change = ((umtmvsDF['UMTMVS'].loc['2009-01-01'] - umtmvsDF['UMTMVS'].loc['2019-01-01']) / (
    umtmvsDF['UMTMVS'].loc['2009-01-01']) * 100)
print ( '\nA1: Total percentage decrease was : %.2f ' % abs ( change ) )

# What was the percentage decrease in value from Jan 2008 to Jan 2009?
change2 = ((umtmvsDF['UMTMVS'].loc['2008-01-01'] - umtmvsDF['UMTMVS'].loc['2009-01-01']) / (
    umtmvsDF['UMTMVS'].loc['2008-01-01']) * 100)
print ( '\nA2: Total percentage decrease was : %.2f ' % abs ( change2 ) )

# What is the month with the least value after 2005?
print ( '\nA3:', umtmvsDF.loc['2005-12-01' :].idxmin () )

# What 6 months have the highest values?
print ( '\nA4:', umtmvsDF.sort_values ( by='UMTMVS', ascending=False ).head ( 6 ) )

# How many millions of dollars were lost in 2008?
print ( '\nA5:', (umtmvsDF.loc['2008-01-01'] - umtmvsDF.loc['2009-01-01']) )

# Create a bar plot showing the average value per year
tempDF3 = umtmvsDF.resample ( 'A' ).mean ()
ax = tempDF3.plot.bar ( title='Average value per year', grid=True, color=(.21, .42, .12),
                        figsize=(12, 10) )
ax.set ( xlabel=Constants.TIME, ylabel=Constants.USD )

ticklabels = [''] * len ( tempDF3.index )
ticklabels[: :5] = [item.strftime ( '%Y' ) for item in tempDF3.index[: :5]]
ax.xaxis.set_major_formatter ( ticker.FixedFormatter ( ticklabels ) )
plt.gcf ().autofmt_xdate ()
plt.show ()
## $$ Had major problems trying to solve the last question, or rather, in formatting the X axis. Use these SO links for reference
## $$: My SO:  https://stackoverflow.com/questions/67693394/unable-to-format-x-ticks-in-pandas-after-resampling
### $$: Check the accepted answer: https://stackoverflow.com/questions/30133280/pandas-bar-plot-changes-date-format/55161772
# What year had the biggest increase in mean value from the previous year's value?
yearly_data = umtmvsDF.resample ( 'A' ).mean ()
shifted_yearly_data = yearly_data.shift ( 1 )
change = yearly_data - shifted_yearly_data
print ( change )
print ( '\n A7: The biggest change was on : {} \n\tIt\'s value was : {} '.format ( change['UMTMVS'].idxmax (),
                                                                                   change.max () ) )

# Plot out the yearly rolling mean on top of the original data
ax = umtmvsDF['UMTMVS'].plot ()
umtmvsDF.rolling ( window=12 ).mean ()['UMTMVS'].plot ( legend=True, color=(.92, .01, .01), grid=True,
                                                        label='Rolling average (yearly)', ls='-.' )
ax.set ( ylabel=Constants.USD, xlabel=Constants.TIME )
plt.show ()

# BONUS QUESTION
# Some month in 2008, the value peaked before crashing. How long did it take for the value to reach the 2008 peak level?
print ( umtmvsDF.loc['2008' :'01-01-2009'] )
tempDF = umtmvsDF.loc['2008' :'2009']
print ( '\nID MAX', tempDF.idxmax () )
max = tempDF.max ()
kondition = umtmvsDF.loc['2008-06-01' :] > max
tempDF2 = umtmvsDF[kondition].dropna ()
print ( tempDF2 )

print ( len ( umtmvsDF.loc['2008-06-01' :'2014-03-01'] ) )
