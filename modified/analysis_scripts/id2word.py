import os

file_path = os.path.join('dicts_and_encoded_texts','dict_merged.txt')
id = 5


a = open(file_path,'r')

dic = {}

while True:
	line = a.readline()
	line = line[:-1]
	line = line.split('\t')
	if line == None:
		break
	if len(line) == 2:
		dic[int(line[1])] = line[0]

print(dic[id])
