import pandas as pd
database = pd.read_csv('AppleStore.csv')
print('----------------------Columns--------------------------')
print(database.columns) 
print('-------------------------Head-----------------------')
print(database.head())
print('-------------------------Indformation-----------------------')
print(database.info)
print('---------------------------Values---------------------')
print(database['track_name'].value_counts())
print('------------------------------------------------')



