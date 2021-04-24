import os

import numpy as np
import pandas as pd

# NOTE: CSV files can be opened with text editors

df = pd.DataFrame ( np.random.random ( size=(100000, 4) ), columns=["A", "B", "C", "D"] )
print ( df.head () )

# Saving/creating a  CSV file
# The second parameter, "index = False" removes the automatically added index, while the third parameter
# defines the number of significant digits
df.to_csv ( "CreatingCSV.csv", index=False, float_format="%0.4f" )
print ( os.getcwd () )  # To get the location of the CSV file being saved

# Sample data from https://www.kaggle.com/nasa/astronaut-yearbook

df = pd.read_csv ( r'C:\Users\kisho\Desktop\Programming\astronauts.csv' )
print ( df.head () )

# For the file formats to save the data in , HDF5 (*.hdf) is the best and the the largest. Everything else is almost equal in size
