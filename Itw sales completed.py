#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:48:18 2023

@author: obinnauzozie
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

data.info()

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6


ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem



ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased


data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] )/data['CostPerTransaction']

data['Markup'] = ( data['ProfitperTransaction'] )/data['CostPerTransaction']


roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)


my_date ='Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'

print(data['Day'].dtype)

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date  

split_col = data['ClientKeywords'].str.split(',' , expand=True)


#adding extra columns from split client keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]


#replacing opening square brackets with nothing ''
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')


#reduce font size for itemdescription
data['ItemDescription'] = data['ItemDescription'].str.lower()

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files 
data = pd.merge(data, seasons, on= 'Month')


#DROPPING COLUMNS
data = data.drop('ClientKeywords', axis = 1)


#Export into csv
data.to_csv('ITWValueInc_Cleaned.csv', index = False)







data.info()


