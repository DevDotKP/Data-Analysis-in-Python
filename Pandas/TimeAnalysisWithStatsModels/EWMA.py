import json

import pandas as pd
from matplotlib import pyplot as plt

import Constants
import Logging

airlinePassengerVolumeDF = pd.read_html ( Constants.readhtml ( Constants.AIRLINES ).text, index_col='Month',
                                          parse_dates=True )
airlinePassengerVolumeDF = airlinePassengerVolumeDF[0]
airlinePassengerVolumeDF = airlinePassengerVolumeDF.drop ( 'Unnamed: 0', axis=1 )
airlinePassengerVolumeDF = airlinePassengerVolumeDF.dropna ()
toJSON = airlinePassengerVolumeDF.head ( 2 ).to_json ()
print ( toJSON )
parsed = json.loads ( toJSON )
print ( parsed )
Logging.test_logger.info ( "Finalised DF for use", extra=parsed )

airlinePassengerVolumeDF['Thousands of Passengers'].rolling ( window=6 ).mean ().plot ( label='6 month rolling' )

airlinePassengerVolumeDF['Thousands of Passengers'].rolling ( window=12 ).mean ().plot ( label='12 month rolling' )

airlinePassengerVolumeDF['Thousands of Passengers'].ewm ( span=12 ).mean ().plot ( label='EWMA-12', figsize=(20, 5) )

plt.legend ()
plt.show ()
