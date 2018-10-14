#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 20:31:22 2018

@author: descentis
"""

def tab_to_space():
    f = open('output/dicts_and_encoded_texts/dict_merged.txt')
    for line in f:
        with open('node_list.txt','a') as node:
            line = line.replace('\t',',')
            new_line = line.split(',')
           
            line = new_line[1][:-1]+','+new_line[0]+'\n'
            node.write(line)            
    f.close()

    f = open('output/graph/encoded_edges_count_window_size_5.txt')
    for line in f:
        with open('edge_list.txt','a') as node:
            line = line.replace('\t',',')
            node.write(line)            
    f.close()