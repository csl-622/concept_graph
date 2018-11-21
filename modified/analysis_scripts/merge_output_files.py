import os

for i in range(1,25):
	os.system('cp run' + str(i) + '/dicts_and_encoded_texts/dict_merged.txt output/' + str(i) + '_dict_merged.txt')

for i in range(1,25):
	os.system('cp run' + str(i) + '/graph/encoded_edges_count_window_size_5.txt output/' + str(i) + '_graph.txt')
