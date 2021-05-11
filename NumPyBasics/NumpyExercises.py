import numpy as np

# Q1: Create an array of 10 zeroes

q1Array = np.zeros ( 10 )
print ( q1Array )

# Q2: Create an array of 10 ones

q2Array = np.ones ( 10 )
print ( q2Array )

# Q3: Create an array of 10 fives

q3Array = q2Array * 5
print ( q3Array )

# Q4: Create an array of integers from 10 to 50

q4Array = np.arange ( 10, 51, 1 )
print ( q4Array )

# Q5: Create a 3 * 3 matrix with values ranging from 0 to 8

q5Array = np.arange ( 0, 9 ).reshape ( 3, 3 )
print ( q5Array )

# Q6: Create an array of even numbers from 10 to 60
q6Array = np.arange ( 10, 61, 2 )
print ( q6Array )

# Q7 Create a 3 * 3 identity marix
q7Array = np.eye ( 3 )
print ( q7Array )
