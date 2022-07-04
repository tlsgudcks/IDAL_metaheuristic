# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:29:33 2022

@author: parkh
"""
import random
import copy
import pandas as pd
import numpy as np

data_num = 9

p_data = list(np.random.randint(2,8,size=data_num))
d_data = np.random.randint(10,20,size=data_num)
weight = np.random.randint(1,4,size=data_num)

ex = {}
for i in range(1,data_num+1):
    ex["j"+str(i)] = [p_data[i-1],d_data[i-1],weight[i-1]]
df = pd.DataFrame(ex, index = ['p_time','d_date','weight'])
print(df)

df.to_csv('C:/Users/parkh/scheduling2.csv')
df.index = ['p_time','d_date','weight']