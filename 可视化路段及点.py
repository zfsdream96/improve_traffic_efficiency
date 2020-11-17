# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 22:05:20 2020

.format() 可以控制引号内的内容

@author: zfsdr
"""
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

data=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/small_distinct_link_xuqiu_test.csv',encoding='ANSI')

m = folium.Map(location=[30.62,104.07], zoom_start=13,width='100%',height='100%', zoom_control='False',tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}&ltype=6',attr='AutoNavi')
# ref https://www.biaodianfu.com/folium.html

#生成点
for i in range(len(data['Start_Node'])):
    folium.Marker([data.loc[i,'Latitude_Start'],data.loc[i,'Longitude_Start']],tooltip='{ii}'.format(ii=data.loc[i,'Start_Node'])).add_to(m)
#生成线 利用不同的layer控制不同的线在不同的layer
for i in range(len(data['Start_Node'])):
    f=folium.FeatureGroup('{ii}'.format(ii=str(data.loc[i,'Start_Node'])+"-"+str(data.loc[i,'End_Node'])+"-"+str(data.loc[i,'Link'])+"-"+str(data.loc[i,'road'])))
    folium.vector_layers.PolyLine([[data.loc[i,'Latitude_Start'],data.loc[i,'Longitude_Start']],[data.loc[i,'Latitude_End'],data.loc[i,'Longitude_end']]],tooltip='{ii}'.format(ii=str(data.loc[i,'Start_Node'])+"-"+str(data.loc[i,'End_Node'])+"-"+str(data.loc[i,'Link'])+"-"+str(data.loc[i,'road'])),color='red').add_to(f)
    f.add_to(m)
folium.LayerControl().add_to(m)                                                                                             
    #folium.PolyLine([[data.loc[i,'Latitude_Start'],data.loc[i,'Longitude_Start']],[data.loc[i,'Latitude_End'],data.loc[i,'Longitude_end']]],popup='{ii}'.format(ii=data.loc[i,'Link']),color='red').add_to(m)
'''
folium.Marker([30.6237805,104.076743299999], popup='0',tooltip=tooltip).add_to(m)
folium.Marker([30.62020403,104.0717533], popup='1',tooltip=tooltip).add_to(m)
folium.Marker([30.62932893,104.0716317], popup='2',tooltip=tooltip).add_to(m)
folium.PolyLine([[30.6237805,104.076743299999],[30.62020403,104.0717533]],popup='222',color='red').add_to(m)
'''
m.save('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/map.html')