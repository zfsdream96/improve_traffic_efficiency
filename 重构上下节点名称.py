# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:41:40 2020
重构大区域节点名称 生成小区域信息
@author: zfsdr
"""

import pandas as pd

data=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/map_gcj02.csv')

#定义实验范围
#小范围
'''
小范围
lon_small=104.065900
lon_big=104.077005
lat_small=30.61899127
lat_big=30.633739

大范围
lon_small=104.051636
lon_big=104.092005
lat_small=30.606650
lat_big=30.647216
'''


lon_small=104.051636
lon_big=104.092005
lat_small=30.606650
lat_big=30.647216
data=data[data['Longitude_Start']>lon_small]
data=data[data['Longitude_Start']<lon_big]
data=data[data['Latitude_Start']>lat_small]
data=data[data['Latitude_Start']<lat_big]

data=data[data['Longitude_end']>lon_small]
data=data[data['Longitude_end']<lon_big]
data=data[data['Latitude_End']>lat_small]
data=data[data['Latitude_End']<lat_big]

data.loc[:,'road']=0
data=data.reset_index(drop=True) #重构索引



a=0
for i in range(len(data['Longitude_Start'])):
    try:
        if data.loc[i,'Start_Node'] == data.loc[i+1,'Start_Node']:
            data.loc[i,'Start_Node']=a
        else:
            data.loc[i,'Start_Node']=a
            a=a+1
    except:
        data.loc[i,'Start_Node']=a

data['start']=data['Longitude_Start'].map(str)+","+data['Latitude_Start'].map(str) 
data['end']=data['Longitude_end'].map(str)+","+data['Latitude_End'].map(str) 


#可以用来判断是不是另外一个column有重复的值
for c in range(len(data['Longitude_Start'])):
    q=data['end'].isin([data['start'][c]])
    data.loc[q,'End_Node']=data['Start_Node'][c]
data=data.drop(['start','end'],axis=1)
data.to_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/big_distinct_linktest.csv',encoding='ANSI') 

lon_small2=104.065900
lon_big2=104.077005
lat_small2=30.61899127
lat_big2=30.633739
data_small=data
data_small=data_small[data_small['Longitude_Start']>lon_small2]
data_small=data_small[data_small['Longitude_Start']<lon_big2]
data_small=data_small[data_small['Latitude_Start']>lat_small2]
data_small=data_small[data_small['Latitude_Start']<lat_big2]
data_small=data_small[data_small['Longitude_end']>lon_small2]
data_small=data_small[data_small['Longitude_end']<lon_big2]
data_small=data_small[data_small['Latitude_End']>lat_small2]
data_small=data_small[data_small['Latitude_End']<lat_big2] 

data_small.to_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/small_distinct_link.csv',encoding='ANSI')         