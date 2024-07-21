""""How do I select a subset of a DataFrame?"""

import pandas as pd

""""for working with columns"""
titanic=pd.read_csv("titanic.csv")

#for the particular row we just use the squuare bracket and name of the column
ages=titanic['Age']
print(ages.head())#print the values


t=type(ages.head())#print it type which is in the form of series
print(t)

print(ages.shape)

#for print the more particular row more than one
age_sex=titanic[['Age','Sex']]
print(age_sex.head())

#print the data type of the of both column
t=type(titanic.head())
print(t)

print(age_sex.shape)

""""for working wiht rows"""
#for selecting the rows we give the conditon inside the square bracket for the given condition
above_35=titanic['Age']>35 #only give the entire list in true or false
print(above_35)
print(above_35.shape)

above_35_row=titanic[titanic['Age']>35]#for print the entire row we use the one more time variable name of the file
print(above_35_row.head())
print(above_35_row.shape)

""""I’m interested in the Titanic passengers from cabin class 2 and 3."""
cabin_2_3=titanic[titanic['Pclass'].isin([2,3])]#if we want to find the particular data from the column present in the particular column name we use thte isin method and mention the number we want to see and in the column
print(cabin_2_3.head())

#we also write the similar method by using the different condition i.e(||,&&,==,...)
class_2_3=titanic[(titanic['Pclass']==2) | (titanic['Pclass']==3)]
print(class_2_3.head())

""""The notna() function in pandas is used to detect non-missing values in a DataFrame or Series. It is the inverse of the isna() function, which is used to detect missing values (such as NaN)."""
age_not_na=titanic[titanic['Age'].notna()]
print(age_not_na.head)
print(age_not_na.shape)


""""How do I select specific rows and columns from a DataFrame?"""

""""names of the passengers older than 35 years."""
adult_names=titanic.loc[titanic['Age']>35,"Name"]#The loc/iloc operators are required in front of the selection brackets [].
print(adult_names.head())

# rows 10 till 25 and columns 3 to 5.
slice_row_column=titanic.iloc[9:25,2:5]
print(slice_row_column)

titanic_iloc=titanic.iloc[0:3,3]='anonymous'
print(titanic.head())
