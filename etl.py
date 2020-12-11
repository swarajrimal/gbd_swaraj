import os
import pandas as pd

#set the working directory. wdpath should be set as current working diretory
wdpath = '/Users/swaraj/Desktop/gbd'
os.chdir(wdpath)

#reading the CSV file
file = pd.read_csv("ratnapark.csv")

#removing the trailing space from the column name
file.rename(columns={'particulate_matter ':'particulate_matter'}, inplace=True)

#check for missing values
print(file.isnull().value_counts())

#describing the fields
print(file.describe())

#checking data types of columns
print(file.dtypes)

#converting datetime column to datetime data type
file['datetime'] = pd.to_datetime(file['datetime'])

#cleaning the 'value' column to contain only the floating point numbers and removing the rest
df = file[file['value'].str.contains('^[-+]?[0-9]*\.?[0-9]+$')]

#converting 'value' column to floating point data type
df['value'] = df['value'].apply(pd.to_numeric)
print(df.dtypes)

#stats of 'value' column
print(df['value'].describe())

#removing outliers of 'value' column
q1=df['value'].quantile(0.25)
q3=df['value'].quantile(0.75)
iqr=q3-q1
whisker_high = q3+1.5*iqr
print(df.shape)
df1 = df[df['value']<whisker_high]
print(df1.shape)
print()
print(df1['value'].describe())

#reseting the index number after removing unwanted rows
df1.reset_index(drop=True, inplace=True)
print(df1)

#store table to a json file
df1.to_json("ratnapark.json")


