from datetime import datetime

import numpy as np
import pandas as pd

my_year = 2021
my_month = 5
my_date = 18
my_hour = 14
my_min = 2021
my_year = 2021

myDate = datetime ( my_year, my_month, my_date )
print ( myDate )  # Since the time is not given, it defaults to 00:00:00
print ( '\nWhat day of the month is it? : ', myDate.day )

# NumPy's dateTime module is much better than Python's dateTime format
npDateTime = np.array ( ['2021-05-03', '2021-05-04', '2021-05-05'],
                        dtype='datetime64' )  # The dtype has to be defined for the numpy array to be converted to a date array
# By default, the precision of datetime64 is 'Day'. This can be changed however. Eg: To change it to year, dtype = 'datetime64[Y]'
print ( '\nNumpyDate: ', npDateTime )

# np.arange can also be used for dates as well
print ( np.arange ( '2018-01-20', '2018-02-28', 7, dtype='datetime64[D]' ) )
print ( '\nnp.arange for years:', np.arange ( '1964', '1994', 10, dtype='datetime64[Y]' ) )

# Panda's dateTime module

pandaDateTime = pd.date_range ( start='2021-05-18', periods=30,
                                freq='D' )  # Default precision for dateTIme module of Pandas is ns
print ( pandaDateTime )

pandaDateTime = pd.to_datetime ( ['Jan 2, 2018'] )
print ( pandaDateTime )

# Working with different date Time formats
# We can define formats. Pandas defaults to the US date format
pandaDateTime = pd.to_datetime ( ['1.5.2021'], format='%d.%m.%Y' )
print ( pandaDateTime )


data = np.random.rand ( 3, 2 )
cols = ['A', 'B']
indx = pd.date_range ( '24-05-2021', periods=3, freq='D' )
df1 = pd.DataFrame ( data=data, index=indx, columns=cols )

print ( '\n', df1 )
# %%
print ( 'Hello' )

# TimeResampling
