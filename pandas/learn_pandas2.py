"""How do I read and write tabular data?"""
import pandas as pd
#read csv function is to store the data and stored as csv format(comma separated values)
titanic=pd.read_csv('titanic.csv')
print(titanic)

#print the first 8 rows from the top for the last if we want to see the data form the last we used the tail method
print(titanic.head(8))
print(titanic.tail(5))

#for check the each column data type we used the dtype
print(titanic.dtypes)


titanic.to_excel('titanic.xlsx',sheet_name='passengers',index=False)

titanic_loaded=pd.read_excel('titanic.xlsx',sheet_name="passengers")
print(titanic_loaded.head())
