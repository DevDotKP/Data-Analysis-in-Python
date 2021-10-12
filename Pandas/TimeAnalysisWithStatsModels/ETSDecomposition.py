import pandas as pd
from matplotlib import pyplot as plt
from pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose

import Constants

airlinePassengerVolumeDF = pd.read_html ( Constants.readhtml ( Constants.AIRLINES ).text, index_col='Month',
                                          parse_dates=True )
airlinePassengerVolumeDF = airlinePassengerVolumeDF[0]
airlinePassengerVolumeDF = airlinePassengerVolumeDF.drop ( 'Unnamed: 0', axis=1 )
airlinePassengerVolumeDF = airlinePassengerVolumeDF.dropna ()
airlinePassengerVolumeDF.plot ()

result = seasonal_decompose ( airlinePassengerVolumeDF['Thousands of Passengers'], model='multiplicative' )
rcParams['figure.figsize'] = 12, 5

result.trend.plot ( label='Trend', color=(.95, .88, .76) )

plt.show ()
