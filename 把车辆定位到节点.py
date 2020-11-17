# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:22:22 2020
将位置定义成点
@author: zfsdr
"""

from math import radians, cos, sin, asin, sqrt
import pandas as pd
 
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000


data1=pd.read_excel('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/20191211new/需求/合并.xlsx')
data2=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/big_distinct_link.csv')
data2=data2.drop_duplicates(['Start_Node'])
data2=data2.set_index(data2['Start_Node'])
d=[]

for i in range(len(data1['o_gps'])):
    a=[]
    aa=[]
    lon=float(data1['o_gps'][i][1:data1['o_gps'][i].rfind(",")])
    lat=float(data1['o_gps'][i][data1['o_gps'][i].rfind(",")+1:data1['o_gps'][i].rfind("]")])
    lon1=float(data1['d_gps'][i][1:data1['d_gps'][i].rfind(",")])
    lat1=float(data1['d_gps'][i][data1['d_gps'][i].rfind(",")+1:data1['d_gps'][i].rfind("]")])
    for c in data2['Start_Node']:
        lon2=data2.loc[c,'Longitude_Start'].tolist()
        lat2=data2.loc[c,'Latitude_Start'].tolist()
        a.append(haversine(lon, lat, lon2, lat2))
        aa.append(haversine(lon1, lat1, lon2, lat2))
    b=a.index(min(a))
    bb=aa.index(min(aa))
    print(i)
    data1.loc[i,'o']=b
    data1.loc[i,'d']=bb
    data1.loc[i,'hash']=b*10000+bb

data1.to_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/合并_初始化上下车点.csv',encoding='ANSI')
