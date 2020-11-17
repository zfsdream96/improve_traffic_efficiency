# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:19:46 2020

用来合并gps为高德地图可视化能用的坐标

@author: zfsdr
"""

import pandas as pd

data=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/map_gcj02.csv')
data=data[data['Longitude_Start']>104.051636]
data=data[data['Longitude_Start']<104.092005]
data=data[data['Latitude_Start']>30.606650]
data=data[data['Latitude_Start']<30.647216]
data['position']=data['Longitude_Start'].map(str)+","+data['Latitude_Start'].map(str) #坐标合并
data_eliminate_duplicate_position=data.drop_duplicates(['Start_Node'])
gaode_position=data_eliminate_duplicate_position[['Start_Node','position']]

gaode_position.to_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/实验范围.csv',encoding='UTF-8')