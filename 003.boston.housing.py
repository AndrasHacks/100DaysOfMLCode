#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:24:02 2020

@author: andras
"""

import pandas as pd
import seaborn as sns

df_train = pd.read_csv('./datasets/BostonHousing.csv')

print('Describe the datapoints:')
print(df_train.columns)
print()

# Describe the target variable
print('Median value of owner-occupied homes in $1000\'s: ')
print(df_train['medv'].describe())

sns.distplot(df_train['medv'])
print('Skewness: %f' % df_train['medv'].skew())
print('Kurtosis: %f' % df_train['medv'].kurt())

# average number of rooms per dwelling
var = 'rm'
data = pd.concat([df_train['medv'], df_train['rm']], axis = 1)
data.plot.scatter(x = var, y = 'medv')


