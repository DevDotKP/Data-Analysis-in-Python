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

print ( np.arange ( 0, 10, 2 ) )

print ( np.random.rand ( 3, 3 ) )  # Used to generate a random array or matrix (2D array)

print ( np.random.normal ( 150, 35, 9 ) )  # Generates 9 numbers for a dataset with  the mean of 150 and std.dev of  35

print ( np.random.randint ( 10, 15, 10 ) )

np.random.seed (
    101 )  # Used to generate the same random numbers in different computers. The next line will have the same O/P in every single computer
print ( np.random.rand ( 4 ) )

arbitraryArray = np.arange ( 0, 100, 4 )

print ( arbitraryArray )  # As expected, prints 25 values as 1D array

arbitraryArray = arbitraryArray.reshape ( 5, 5 )  # Reshapes the 1D array to a 5*5 array

print ( arbitraryArray )  # Prints the values as 5*5 array

print ( arbitraryArray.min () )

print ( arbitraryArray.max () )
