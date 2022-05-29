# -*- coding: utf-8 -*-
"""
Created on Sun May 29 23:55:26 2022

@author: 79634
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'Admission_Predict.csv'
data = pd.read_csv(file, sep=",")
print(data.head())

print(data.info())

print('Количество пропущенных значений')
print(data.isnull().sum())

print(sns.violinplot(x=data['University Rating']))

data['CGPA'].replace('No', 0,inplace=True)
data['CGPA'].replace('Yes', 1, inplace=True)

print(data['CGPA'].astype(int))

print(data.corr())

print(sns.heatmap(data.corr(), annot=True))