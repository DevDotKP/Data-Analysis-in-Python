import json

import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

import Constants
import Logging

airlinePassengerVolumeDF = pd.read_html ( Constants.readhtml ( Constants.AIRLINES ).text, index_col='Month',
                                          parse_dates=True )
airlinePassengerVolumeDF = airlinePassengerVolumeDF[0]
airlinePassengerVolumeDF = airlinePassengerVolumeDF.drop ( 'Unnamed: 0', axis=1 )
airlinePassengerVolumeDF = airlinePassengerVolumeDF.dropna ()

span = 12
alpha = 2 / (span + 1)

airlinePassengerVolumeDF['EWMA'] = airlinePassengerVolumeDF['Thousands of Passengers'].ewm ( alpha=alpha,
                                                                                             adjust=False ).mean ()
model = SimpleExpSmoothing ( airlinePassengerVolumeDF['Thousands of Passengers'] )
fitted_model = model.fit ( optimized=False, smoothing_level=alpha )
airlinePassengerVolumeDF['SES12'] = fitted_model.fittedvalues.shift ( -1 )
toJSON = airlinePassengerVolumeDF.head ( 5 ).to_json ()
print ( toJSON )
parsed = json.loads ( toJSON )
print ( parsed )
Logging.test_logger.info ( 'After adding the SES: {} '.format ( parsed ) )

ax = airlinePassengerVolumeDF['EWMA'].plot ( label='EWMA' )
airlinePassengerVolumeDF['SES12'].plot ( label='SES12' )
ax = ax.set ( xlabel=Constants.TIME, ylabel='PassengerVolume ( Thousands)' )
plt.show ()

airlinePassengerVolumeDF['DES12'] = ExponentialSmoothing ( airlinePassengerVolumeDF['Thousands of Passengers'],
                                                           trend='add' ).fit ().fittedvalues.shift ( -1 ).plot (
    label='Normal exponentialSmoothing' )
plt.show ()
print ( airlinePassengerVolumeDF.head () )

airlinePassengerVolumeDF[['Thousands of Passengers', 'EWMA', 'SES12', 'DES12']].iloc[:24].plot ( figsize=(12, 5),
                                                                                                 label='Comparison of smoothing methods',
                                                                                                 legend=(2, 1) )
plt.show ()

Logging.test_logger.exception ( airlinePassengerVolumeDF.head () )

try :
    populationDF = pd.read_excel ( r'C:\Users\kisho\Downloads\WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES.xlsx',
                                   engine='openpyxl', header=16, sheet_name='ESTIMATES' )
    # populationDF = populationDF.set_index ( 'Index')
    filteredPopulationDF = populationDF[populationDF['Type'].str.contains ( 'Country/Area' )]

    southAsiaDataDF = filteredPopulationDF[filteredPopulationDF['Parent code'] == 5501]
    southAsiaDataDF.drop ( columns=['Variant', 'Notes', 'Index'], inplace=True )
    southAsiaDataDF.rename ( columns={'Region, subregion, country or area *' : 'Country'}, inplace=True )
    southAsiaDataDF.set_index ( 'Country' )
    print ( southAsiaDataDF.head () )
    southAsiaDataDF['1970'].plot ()
    plt.tight_layout ()
    plt.show ()
    # print()
    # southAsiaDataDF[southAsiaDataDF['Country'].str.contains('India')].plot()
    # plt.show()

    # pivotSouthAsia = southAsiaDataDF.pivot_table('Country')
    # print('\n\n Columns',pivotSouthAsia)
except Exception as e :
    print ( e.args )
