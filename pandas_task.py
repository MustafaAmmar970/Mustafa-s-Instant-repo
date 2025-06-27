import pandas as pd
#sort by index
data = pd.read_csv(".\AD.csv")
data.set_index('ID',inplace=True)
data.sort_index(ascending=False,inplace=True)
print(data)
#sort by column
data.reset_index(inplace=True) 
data.sort_values(by='Height_cm',inplace=True)
print(data)
