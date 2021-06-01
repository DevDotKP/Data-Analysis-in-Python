import requests

USD = 'USD($)'
TIME = 'Time'
# URLs
STARBUCKS = 'https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/Reference/starbucks.csv'
MILK_PRODUCTION = 'https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/Reference/monthly_milk_production.csv'
UMTMVS = 'https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeSeries/Reference/UMTMVS.csv'
MACRODATA = 'https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/TimeAnalysisWithStatsModels/Reference/macrodata.csv'

HEADER = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest"
}

PRODUCTION = 'Production'



def readhtml(url) :
    r = requests.get ( url=url, headers=HEADER )
    return r
