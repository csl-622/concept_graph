#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created: 25-10-2018
@author: pratik-chhajer
'''

from word_processing import *
from sentence_processing import *
from wordpair_processing import *
import util, multi_processing 
import time
import os

if __name__ == '__main__':
	max_window_size = 5
	process_num = 5
	min_count = 1
	max_vocab_size = 100000
	safe_files_number_per_processor = 200
	start_time = time.time()

	input_folder = 'input'
	processed_folder = "processed"
	dicts_folder = "dicts_and_encoded_texts"
	edges_folder = "edges"
	graph_folder = "graph"
	
	util.mkdir_p(processed_folder)
	util.mkdir_p(dicts_folder)
	util.mkdir_p(edges_folder)
	util.mkdir_p(graph_folder)
	
	util.preProcessing(input_folder,processed_folder)
	
	wp = WordProcessing(output_folder=dicts_folder)
	merged_dict = wp.apply(data_folder=processed_folder, process_num=process_num)
	sp = SentenceProcessing(dicts_folder=dicts_folder, output_folder=edges_folder,
							max_window_size=max_window_size, local_dict_extension='.dicloc')
	word_count_all = sp.apply(data_folder=dicts_folder, process_num=process_num)
	wpp = WordPairsProcessing(max_vocab_size=max_vocab_size, min_count=min_count,
							  dicts_folder=dicts_folder, window_size=max_window_size,
							  edges_folder=edges_folder, graph_folder=graph_folder,
							  safe_files_number_per_processor=safe_files_number_per_processor)
	result = wpp.apply(process_num=process_num)
	print('time in seconds:', util.count_time(start_time))
