import os
import pickle

with open('dict12.pickle','rb') as handle:
	Dictionary = pickle.load(handle)

print('Dictionary reading done!')

with open('graph12.pickle','rb') as handle:
	Edges = pickle.load(handle)

print('Edges reading done!')

with open('dict24.txt','rb') as handle:
	Dictionary_ = pickle.load(handle)

print('Dictionary_ reading done!')

with open('graph24.txt','rb') as handle:
	Edges_ = pickle.load(handle)

print('Edges_ reading done!')

Id2Id = {}

for key, val in Dictionary_.items():
	if key in Dictionary:
		Id2Id[val] = Dictionary[key]
	else:
		Id2Id[val] = len(Dictionary)

print('Dictionary done!')

for key, val in Edges_.items():
	a = Id2Id[key[0]]
	b = Id2Id[key[1]]
	if (a,b) in Edges:
		Edges[(a,b)] += val
	else:
		Edges[(a,b)] = val

print('Graph done!')

with open('dict.pickle','wb') as handle:
	pickle.dump(Dictionary,handle)

print('Dictionary dumped!')

with open('graph.pickle','wb') as handle:
	pickle.dump(Edges,handle)

print('Graph dumped!')

print('Dumping done!')

with open('dict.txt', 'a') as out:
	for key, val in Dictionary.items():
		out.write(key + '\t' + str(val) + '\n')

print('dict.txt done')

with open('graph.txt', 'a') as out:
	for key, val in Edges.items():
		out.write(str(key[0]) + '\t' + str(key[1]) + '\t' + str(val) + '\n')

print('graph.txt done')
