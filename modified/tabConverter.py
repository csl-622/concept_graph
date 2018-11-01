#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 20:31:22 2018

@author: descentis
"""

def tab_to_space():
    f = open('dicts_and_encoded_texts/dict_merged.txt')
    input_ID = open('dicts_and_encoded_texts/valid_vocabulary_min_count_50_vocab_size_200.txt')
    
    input_list = []
    for num in input_ID:
        input_list.append(num[:-1])
    
    
    for line in f:
        with open('node_list.txt','a') as node:
            line = line.replace('\t',',')
            new_line = line.split(',')
            if(new_line[1][:-1] in input_list):
                line = new_line[1][:-1]+','+new_line[0]+'\n'
                node.write(line)            
    f.close()

    f = open('graph/encoded_edges_count_window_size_2.txt')
    for line in f:
        with open('edge_list.txt','a') as node:
            line = line.replace('\t',',')
            node.write(line)            
    f.close()

tab_to_space()