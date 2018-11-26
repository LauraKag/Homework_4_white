# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:15:45 2018

@author: laura
"""

#%%
#Create a function non_connected to find non-connected nodes in a graph.
graph={
       "a":["b","c"],
       "b":["d"],
       "c":["d"],
       "d":["e"],
       "e":[],
       "f":[]
       }
#In this case: f is not connected.

def non_connected(graph):
    values=graph.values()
    keys=graph.keys()
    values2=[]
    for i in values:
        for j in i:
            values2.append(j)
    
    for key in keys:
        if key not in values2 and graph[key]==[]:
            return key
    
        
    