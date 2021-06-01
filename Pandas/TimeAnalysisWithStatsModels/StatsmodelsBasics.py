import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter

import Constants

statsDF = pd.read_html ( Constants.readhtml ( Constants.MACRODATA ).text, index_col=0, parse_dates=True )
statsDF = statsDF[0]
statsDF.rename ( columns={'Unnamed: 1' : 'Date'}, inplace=True )
statsDF['Date'] = pd.to_datetime ( statsDF['Date'] )
statsDF.set_index ( 'Date', inplace=True )
statsDF['realgdp']['2005' :].plot ( title='GDP vs time', color=(.76, .86, .21) )
gdp_cycle, gdp_trend = hpfilter ( statsDF['realgdp'], lamb=1600 )
statsDF['GDPtrend'] = gdp_trend
statsDF['GDPtrend']['2005' :].plot ( label='GDP trend', ls='--', color=(.98, .12, .53) )
plt.show ()
