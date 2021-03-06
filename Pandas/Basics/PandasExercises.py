import pandas as pd

try :
    # Q1: Read the population_by_county.csvfile into a dataframe called pop
    pop = pd.read_csv (
        r'C:\Users\kisho\Desktop\Programming\Learning\Data analysis with Python\UDEMY_TSA_FINAL\Data\population_by_county.csv' )

    # Q2: Show the head
    print ( '\n\r\tA2\n', pop.head () )

    # Q3: What are the column names?
    print ( '\n\r\tA3\n' )
    print ( pop.info () )

    # Q4: How many states are represented in this data?
    print ( '\n\r\tA4\n', pop['State'].nunique () )

    # Q5: List of all states in the data
    print ( '\n\r\tA5\n', pop['State'].unique () )

    # Q6: What are the five most common county names(2010)?
    print ( '\n\r\tA6\n', pop['County'].value_counts ().head ( 5 ) )

    # Q7:What are the five most populated counties in the data (2010)?
    print ( '\n\r\tA7\n', pop.sort_values ( by='2010Census', ascending=False ).head ( 5 ) )

    # Q8: How many counties have a population of more than a million(2010)?
    kondition = pop['2010Census'] > 1000000
    print ( '\n\r\tA8\n', pop[kondition]['County'].count () )

    # Q9: Add a column that calculates the percent change between 2010 and 2017 census
    pop['percentageChange'] = (((pop['2017PopEstimate'] - pop['2010Census']) / pop['2010Census']) * 100)
    print ( '\n\r\tA9\n', pop )

    # Q10: What states have the highest estimated percent change between 2010 and 2017?
    pop['absoluteChange'] = pop['percentageChange'].abs ()

    print ( pop )
    print ( pop.sort_values ( by='absoluteChange', ascending=False ).head ( 5 ) )

    newdf = pop.groupby ( by='State' ).sum ()
    newdf['percentageChange'] = (((newdf['2017PopEstimate'] - newdf['2010Census']) / newdf['2010Census']) * 100)
    newdf['absoluteChange'] = newdf['percentageChange'].abs ()
    print ( newdf.sort_values ( by='absoluteChange', ascending=False ).head ( 5 ) )

    print ( '\nHello\n', newdf )

    # Q11: What are the 5 most populated states according to the data?
    print ( '\n\r\tA11\n',
            pop.groupby ( by='State' ).sum ().sort_values ( by='2010Census', ascending=False ).head ( 5 ) )


    # Q12: How many counties do not have the word 'County' in their names?
    def check_county(name) :
        return 'County' not in name


    print ( '\n\r\tA12\n', sum ( pop['County'].apply ( check_county ) ) )

    # Method 2: One liner:
    print ( '\n\r\t Better method: A12\n', sum ( pop['County'].apply ( lambda name : 'County' not in name ) ) )


except Exception as e :
    print ( 'Error detected!{} \n {} \n {}'.format ( e.args, e.__class__, e.__doc__ ) )
