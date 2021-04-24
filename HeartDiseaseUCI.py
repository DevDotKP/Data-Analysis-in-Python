# Creating and formatting data

import numpy as np
import pandas as pd

df = pd.read_csv ( r"C:\Users\kisho\Desktop\Programming\heart.csv" )
data = np.random.random ( size=(3, 3) )

print ( data )

df = pd.DataFrame ( data=data, columns=["A", "B", "C"] )
print ( df )

df = pd.DataFrame ( data={"S.no" : [1, 2, 3], "Name" : ["Kamala Devi", "Pattabhiraman", "Upasana"]} )
print ( df )

dtype = [(("S.no"), np.int), ("Name", (np.str, 20))]

data = np.array ( [(1, "Kamala Devi"), (2, "Pattabhiraman"), (3, "Upasana")], dtype=dtype )
print ( data )
df = pd.DataFrame ( data )
print ( df )
