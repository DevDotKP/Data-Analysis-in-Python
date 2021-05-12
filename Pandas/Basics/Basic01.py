import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

myList = [10, 20, 30]

arr = np.array ( myList )

print ( arr )

d = {'d' : 10, 'e' : 20, 'f' : 30}  # Defining a dictionary

print ( pd.Series ( data=myList ) )  # Pandas automatically names the columns and rows if not provided

print ( pd.Series ( data=arr, index=labels ) )  # 'indes=' names the rows

print ( d )

print ( pd.Series ( data=d ) )  # A dictionary shows up correctly

dictADBMoney = {'India' : 100, 'China' : 190, 'Japan' : 130}
dictSCOMoney = {'India' : 40, 'China' : 210, 'Bangladesh' : 15}
ADBMoney = pd.Series ( data=dictADBMoney )
SCOMoney = pd.Series ( data=dictSCOMoney )

totalMoney = ADBMoney + SCOMoney  # Provides the value of variables common to both the series'. Otherwise, the result is NaN

print ( totalMoney )
