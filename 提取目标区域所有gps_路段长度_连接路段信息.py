# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:29:58 2020

@author: zfsdr
"""

import pandas as pd

data=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/big_distinct_link.csv')

data=data[data['Longitude_Start']>104.065900]
data=data[data['Longitude_Start']<104.077005]
data=data[data['Latitude_Start']>30.61899127]
data=data[data['Latitude_Start']<30.633739]

data=data[data['Longitude_end']>104.065900]
data=data[data['Longitude_end']<104.077005]
data=data[data['Latitude_End']>30.61899127]
data=data[data['Latitude_End']<30.633739]
data.loc[:,'road']=0

data.to_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/目标小区域所有信息22.csv')