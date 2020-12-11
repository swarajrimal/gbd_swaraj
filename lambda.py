import os
import pandas as pd

#set the working directory. wdpath should be set as current working diretory
wdpath = '/Users/swaraj/Desktop/gbd'
os.chdir(wdpath)

#reading the JSON file
df = pd.read_json("ratnapark.json")

#using lambda funcion to append a character to all rows
df['particulate_matter']=df.apply(lambda x: '_'+x['particulate_matter'], axis=1)
print(df.head())
