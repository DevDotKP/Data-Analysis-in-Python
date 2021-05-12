import numpy as np

arrayOne = np.arange ( 0, 11 )

print ( arrayOne )
arrayOne = arrayOne ** 2  # Squares the array values
print ( arrayOne )

arrayOneSliceOne = arrayOne[:4]
print ( arrayOneSliceOne )  # Prints values from the starting of the array till the 3rd index

arrayOneSliceOne[:] = 99
print ( arrayOneSliceOne )  # Prints each element as 99

print ( arrayOne )  # Now, the first 4 values(0,1,2,3 indices) have their values changed in the original array as well

arrayOneCopy = arrayOne.copy ()

arrayOneCopy[:] = 11  # To avoid changing the original data, we have to explicitly copy it

print ( arrayOneCopy )  # Prints all values as 11
print ( arrayOne )  # Prints the values as they ere post the slicing

twoDArray = np.arange ( 0, 25 ).reshape ( 5, 5 )
print ( twoDArray )

twoDArray[4, 4] = 101  # Accessing and modifying row 4, column 4 cell
print ( twoDArray )  # Shows the changed value now

print ( twoDArray[:2,
        3 :] )  # Prints the sub-matrix from the beginning row (0) till, but not including, now 2 and from column 3 till the last column

# Conditional selection

kondition = arrayOne > 25

print ( kondition )  # Prints if the values in arrayOne are more than 25 or not as 'True' and 'False'

print ( arrayOne[kondition] )  # Prints only those values which satisfy the condition

print ( twoDArray.sum () )

print ( twoDArray.sum ( axis=0 ) )  # Gives the sums of the columns

print ( twoDArray.sum ( axis=1 ) )  # Gives the sum of rows
