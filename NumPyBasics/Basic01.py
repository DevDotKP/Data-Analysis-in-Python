import numpy as np

myList = [1, 2, 3]  # This is a normal array/ list

print ( type ( myList ) )  # This will return the dataType as 'list'

print ( np.array ( myList ) )

npArray = np.array ( myList )

print ( type ( npArray ) )  # The dataType/ class is now numpy.ndArray, or simply a NumPy array

print ( npArray )

nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print ( nestedList )  # Prints exactly the way it was defined, as in, prints in a single row

print ( np.array ( nestedList ) )
# np.array(nestedList) print a 3*3 array with the values in 3 rows and 3 columns. This is called a matrix

myMatrix = np.array ( (nestedList) )

print ( myMatrix.shape )
