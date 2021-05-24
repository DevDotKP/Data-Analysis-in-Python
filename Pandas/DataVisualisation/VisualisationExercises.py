import matplotlib.pyplot as plt
import pandas as pd
import requests

# Reading exercies file

url = 'https://github.com/DevDotKP/Data-Analysis-in-Python/blob/Test/Pandas/DataVisualisation/df3.csv'

header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest"
}

r = requests.get ( url=url, headers=header )

df = pd.read_html ( r.text )
df = df[0]  # Converting to a dataframe
print ( df )
# Q1: Create a scatter plot of 'produced' vs 'defective'
df.plot.scatter ( x='produced', y='defective', marker='H', c='k' )
plt.show ()

# Q2: Create a histogram of the produced column
df['produced'].plot.hist ()
plt.show ()

# Q3: Recreate the histogram made in Q2, tightening the x-axis and adding edge colours betweem the bars
df['produced'].plot.hist ( edgecolor='firebrick' ).autoscale ( axis='x', tight=True )
plt.show ()
# Q4: Create a boxplot that shows produced for each weekday
df[['produced', 'weekday']].boxplot ( by='weekday' )
plt.show ()

# Q5: Create a KDE plot of the defective columm
df['defective'].plot.kde ()
plt.show ()

# Q6: For the above KDE plot, figure out how to increase the landwidth and make the linestyle dashed
df['defective'].plot.kde ( ls='--' )
plt.show ()

# Q7: Create a blended area plot of all the columns for the rows upto 30
df[0 :30].plot.area ( stacked=False, grid=True )
plt.show ()

# Moving the legend outside
ax = df[0 :30].plot.area ( stacked=True )
ax.legend ( bbox_to_anchor=(1, 1) )
plt.show ()
