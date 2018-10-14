#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:42:05 2018

@author: descentis
"""
from run_script import runScript
from text_preprocessing import preProcessing
from tabConverter import tab_to_space
from graph_fromcsv import graph_creator
from graph_analysis import network_analysis
'''
Following function removes all the punctuation from the file and stores it in the data directory
'''

print("=====Preprocessing the raw data=====")
preProcessing('raw_data')
print("====Running the corpus2graph packeage to generate the word co-occurrence network====")
print("====Please wait... Depending on the dataset, it may take some time====")
runScript()
print("====Cleaning the Dataset of generated network====")
tab_to_space()
print("==== Creating the Concept Graph G ====")
graph_creator()
#print("==== Testing the documents present in 'test_doc' by creating the graph H through it ====")
#network_analysis()
#print("Completed!!!")