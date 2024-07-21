""""What kind of data does pandas handle?"""
import pandas as pd

""""creating the simple one line data """
a=pd.DataFrame({'A':[1,2,3]})
print(a)


""""creating the number of datas stored in the form of tabular form """
df=pd.DataFrame(
    {
        'Name':[
            "Mujtaba Malik",
            "Muhammad Maaz",
            "Alishba"
        ],
        'Age':[20,18,17],
        'Gender':["male",'male','female']
    }
)
print(df)

""""print the particular object by using it's keys"""
print(df['Age'])

""""creating the series from the scratch"""
ages=pd.Series([21,52,60],name='age')
print(ages)

print(ages.max())#for highest maximum number present in the series
print(ages.min())#for lowest minimum values present in the series

""""describe is the method provides the quick overview of the numerical data in a data frame only work with data having the numerical values"""
print(df.describe())