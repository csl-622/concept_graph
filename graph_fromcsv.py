#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:49:19 2018

@author: descentis
"""

import networkx as nx

def graph_creator():
    node_list = []
    edge_list = []   

    with open("edge_list.txt", "r") as filestream:   
        for line in filestream:
            currentline = line.split(",")
            new_line = (currentline[0],currentline[1])
            edge_list.append(new_line)
    
    
    with open("node_list.txt","r") as f:
        for line in f:
            l = line.split(",")
            second = l[1]
            second = second[:-1]        
            new_line = (str(l[0]),{'label':second.lower()})
            node_list.append(new_line)
    
    
    G = nx.Graph()
    
    G.add_nodes_from(node_list)
    G.add_edges_from(edge_list)
    
    
    
    nx.write_graphml(G, "outputGraph.graphml")