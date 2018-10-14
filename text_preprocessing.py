#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:56:03 2018

@author: descentis
"""

from nltk.tokenize import RegexpTokenizer
import os

def preProcessing(dir_name):
    files = os.listdir(dir_name)        
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    
    num = 1
    for file_name in files:
        file_name = dir_name+'/'+file_name    
        with open(file_name) as f:
            for i in f:
                line = tokenizer.tokenize(i)            
                line = ' '.join(line)
                output_file = 'data/AA/finalText_'+str(num)+'.txt'
                with open(output_file,'a') as the_file:
                    the_file.write(line)
                    the_file.write(' ')
        num+=1
