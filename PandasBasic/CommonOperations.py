import pandas as pd

df = pd.DataFrame ( {'col1' : [1, 2, 3, 4], 'col2' : [444, 555, 666, 444], 'col3' : ['abc', 'def', 'ghi', 'xyz']} )
print ( df.head () )

print ( "\n", df['col2'].unique () )  # Shows unique values in column 2

print ( "\n", df['col2'].nunique () )  # Shows the number of  unique values in column 2

print ( "\n", df['col2'].value_counts () )  # Shows count of each  value in column 2


def times_two(number) :  # Defining a sample function
    return number * 2


print ( df['col1'].apply ( times_two ) )  # The function multiplies the col1 values by 2

print ( "\n Column names: ", df.columns )

print ( "\n Row range information:", df.index )

print ( "\n DF information\n:", df.info () )

print ( df.sort_values ( by='col2', ascending=False ) )  # Sorting values by col2
