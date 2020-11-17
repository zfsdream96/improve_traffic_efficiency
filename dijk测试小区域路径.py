# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:42:08 2020

@author: zfsdr
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:58:20 2020

@author: zfsdr
"""
import pandas as pd
data=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/big_distinct_link.csv')
data1=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/result1_初始化上下车点.csv',encoding='ANSI')
data3=pd.read_csv('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/all file/目标小区域所有信息.csv',encoding='ANSI')
f = open('C:/Users/zfsdr/OneDrive - stu.scu.edu.cn/Desktop/街区路网优化/上下节点对应的路段.txt','r')
a = f.read()
dict = eval(a)
f.close()

a=[]
new=[[999999999 for j in range(160)] for i in range(160)]
a=new

data=data.set_index(data['Start_Node'])

for i in range(160):
    c=data.loc[i,'End_Node'].tolist()
    cc=data.loc[i,'Length'].tolist()
    if isinstance(c, list):
        c=c
    else:
        c=[c]
    if isinstance(cc, list):
        cc=cc
    else:
        cc=[cc]        
    for ii in range(len(c)):
        a[i][c[ii]]=cc[ii]


from collections import defaultdict
from heapq import *


def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return float("inf"), []

def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. 先求长度
        ## 2. 分解path_queue，以获得最短路径中的传递节点
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 首先记录目标节点;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 记录其他节点，直到源节点。
            right = right[1]
        ret_path.reverse()  ## 3. 最后反转列表，使其成为正常序列。
    return len_shortest_path, ret_path

list_nodes_id = range(0,160)
M=999999999
M_topo = a

edges = []
for i in range(len(M_topo)):
    for j in range(len(M_topo[0])):
        if i != j and M_topo[i][j] != M:
            edges.append((i, j, M_topo[i][j]))  ### (i,j) 是一个链接;M_topo[i][j]这里是1，链接的长度(i,j).


            




start = int(input("请输入起始点："))
end = int(input("请输入终点："))
print("=== Dijkstra算法 ===")
print("找从 %s 到 %s的最短路径:" % (start, end))
length, Shortest_path = dijkstra(edges, start, end)
print('长度 = ', length)
print('最短路径是 ', Shortest_path)

    