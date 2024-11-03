# -*- coding: utf-8 -*-
"""SF salaries EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1459tWX6xtXGkMqpUdm80A-pFnrPI8FZq
"""

import pandas as pd

"""read the dataset using read_csv function from pandas"""

df =pd.read_csv('Salaries.csv')

"""# Dive into data throuh head(), shape, describe"""

df.head()

# to know the count of rows and columns
df.shape

# show some statistics from data
df.describe()

# show data information to know data types and some other information
df.info()

"""# convert some columns from uppercase to lowercase"""

df['JobTitle'] =df['JobTitle'].str.lower()

#convert the Employee Name from uppercase to lowercase
df['EmployeeName'] =df['EmployeeName'].str.lower()

#identify null values
df.isnull().sum()

df.drop(columns='Notes', inplace=True)

df.head()

"""# check for duplicated values"""

#check for duplicate value
df[df.duplicated()]

"""# what is the most frequent 10 jobs found in the dataset

"""

df['JobTitle'].value_counts().head(10)

df['JobTitle'].nunique()

"""# what is the most popular Agencies?"""

df['Agency'].value_counts()

"""# Convert the data type of Base pay column from object on numeric"""

df['BasePay']=pd.to_numeric(df['BasePay'], errors='coerce')

"""# what is the Average salaries in the dataset?"""

df['BasePay'].mean()

"""# what is the maximam salaries in the dataset?


"""

df['BasePay'].max()

"""# what is the minimam  salaries in the dataset?"""

df['BasePay'].min()

"""# what is the maximam salary for each job title sorted from higher to lower ?"""

df.groupby('JobTitle')['BasePay'].max().sort_values(ascending=False).head(10)

"""# what is the average salary for each job title"""

df.groupby('JobTitle')['BasePay'].mean().sort_values(ascending=False).head(10)

"""

# what is the minumam  salary for each job title
"""

df.groupby('JobTitle')['BasePay'].min().sort_values(ascending=False).head(10)

"""# what is the 10 job with the lowest minumam salary ?"""

df.groupby('JobTitle')['BasePay'].min().sort_values(ascending=True).head(10)

"""## **what is the job title of the maximam salary base on base salary (BasePay) **"""

df[df['BasePay']== df['BasePay'].max()]['JobTitle']

"""# What is the highest amount of overtime in the dataset"""

df['OvertimePay']=pd.to_numeric(df['OvertimePay'], errors='coerce')
df['OvertimePay'].max()

"""# What is  the name of employee who has the highest amount of overtime in the dataset"""

df[df['OvertimePay'] == df['OvertimePay'].max()]['EmployeeName']

"""# what is the maximam salary in dataset include benefits and other pays  """

df['TotalPayBenefits']=pd.to_numeric(df['TotalPayBenefits'], errors='coerce')
df['TotalPayBenefits'].max()

"""# what is the job title of the maximam pays and benefits"""

df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['JobTitle']

"""# what is the name of the Employee who has the maximam payment ?"""

df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName']

"""# what is the name of Employee who has the lowest salary in the dataset?

"""

df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]['EmployeeName']

df.query('TotalPayBenefits < 1')

"""# what is (min, mean, max)of salaries between 2011 to 2014"""

df.groupby('Year')['BasePay'].agg(['min','mean','max'])

"""# what are the job titles that occurs only one in the dataset in 2013

"""

(df[df['Year']==2013]['JobTitle'].value_counts() == 1).sum()

"""# how many employees that have chief word in thier titles"""

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

def chief(title):
  if 'chief'in title :
    return True
  else:
      return False

df['JobTitle'].apply(lambda x:chief(x)).sum()
#or
df['JobTitle'].apply(chief).sum()

"""# Is there correlation between job title length and salaries"""

df['title_len']=df['JobTitle'].apply(len)
df['title_len']

df[['title_len','TotalPayBenefits']].corr()