import mysql.connector as connection  # For the SQL connection
import pandas as pd

import requests  # For the HTML connection

try :
    print ( "\n\t\rReading from mySQL" )
    mydb = connection.connect ( host="localhost", database='mydb', user="root", passwd="root", use_pure=True )
    query = "Select * from pandasdataio;"
    sqldf = pd.read_sql ( query, mydb )
    print ( sqldf )
    mydb.close ()  # close the connection

    print ( '\nReading the CSV file\n' )
    csvdf = pd.read_csv (
        r'LocationInYourSystem\example.csv' )
    print ( csvdf )

    clippedRowscvdf = csvdf.loc[3].transpose ()
    print ( clippedRowscvdf )

    print ( '\nReading from HTML\n' )
    # HTML URLs that are copied from the browser have headers built in. When the used tries to access a browser URI from Python, the resource throws a 403
    # So, we provide the raw URI, then mimic the browser headers, so the resource thinks it's a browser trying to access it and allows the connection
    url = 'https://www.worldometers.info/geography/largest-countries-in-the-world/'

    header = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With" : "XMLHttpRequest"
    }
    r = requests.get ( url=url, headers=header )
    htmldf = pd.read_html ( r.text )

    print ( htmldf )




except Exception as e :
    mydb.close ()
    print ( str ( e ) )
