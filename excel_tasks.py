from random import shuffle
import numpy as np
import pandas as pd
#seeting sheet_name to none reads all of them
data =pd.read_excel(".\stocks.xlsx",sheet_name=None,)
print(data['oldstocks'])
print("-----------------------------")
print(data['newstocks'])
#task2 save last 2 columns and 3 rows
data= pd.read_csv('.\AD.csv')
print(data)
last_three = data.tail(3)
print(last_three)
#last_three.to_csv('test2.csv',columns=['Stress_Level','Sleep_Hours'])

#save random data
list_data = data.to_numpy()
shuffled = np.random.permutation(list_data)
shuffled_dataframe = pd.DataFrame(shuffled,columns=['ID','Age','Gender','Height_cm','Weight_kg','BMI','Smoker','Exercise_Freq','Diet_Quality','Alcohol_Consumption','Chronic_Disease','Stress_Level','Sleep_Hours'])
print(shuffled_dataframe)
shuffled_dataframe.to_csv('shuffled_data.csv')