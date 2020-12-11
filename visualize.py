import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set the working directory. wdpath should be set as current working diretory
wdpath = '/Users/swaraj/Desktop/gbd'
os.chdir(wdpath)

#reading the CSV file
df = pd.read_json("ratnapark.json")

pl1 = df[['particulate_matter','value']]

#boxplot of 'values' for different 'particulate_matter' category
bplt = sns.boxplot(y="particulate_matter",x="value", data=pl1)
bplt.set_title("Boxplot of values of Particulate Matter for different categories")
bplt.set_ylabel("Particulate Matter")
bplt.set_xlabel("Values")
plt.show()

#histogram of 'value' to understand its distribution
hplt = sns.histplot(df['value'])
hplt.set_title("Histogram of the values of Particulate Matter")
hplt.set_ylabel("Count")
hplt.set_xlabel("Values")
plt.show()

#grouping the table based on categories of 'particulate_matter'
grp = df.groupby('particulate_matter')

#time-series scatterplot of 'value' for different 'particulate_matter'
tplt = sns.scatterplot(x="datetime", y="value", data=df, hue="particulate_matter")
tplt.set_title("Time-Series scatterplot of particulate matter values by category")
tplt.set_ylabel("Values")
tplt.set_xlabel("Date")
plt.show()


