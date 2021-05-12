import numpy as np
import pandas as pd

df = pd.DataFrame ( {'A' : [1, 2, np.nan], 'B' : [5, np.nan, np.nan], 'C' : [1, 2, 3]} )

print ( df )

print ( df.dropna () )  # Function used to drop NaN values. This'll drop the rows containing NaN

# But what if you want to cull through the columns instead of the rows? Then we use:

print ( df.dropna ( axis=1 ) )  # Used to drop columns with the NaN value

# We can also define tolerance ( a threshold), above which the .dropna() function will work

print ( df.dropna ( thresh=2 ) )  # 2 NaNs are permissible

# Filling in the missing data
print ( '\nFilling in the data\n' )

print ( "\nFilling in with a placeholder\n", df.fillna ( value='PLCAEHOLDER' ) )  # Filling in with a random value
