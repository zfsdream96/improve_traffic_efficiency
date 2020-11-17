# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:05:03 2020

@author: zfsdr
"""



import pandas as pd
data2=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/big_distinct_link.csv')

mapping={}
for i in range(len(data2['Start_Node'])):
    c=10000*data2.loc[i,'Start_Node']+data2.loc[i,'End_Node']
    mapping[c]=[data2.loc[i,'Link']]
a=str(mapping)
with open ('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/上下节点对应的路段.txt','w') as w:
    w.write(a) #write 函数写入必须为str 所以要将上面的dict转化为str