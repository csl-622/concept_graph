import os
import matplotlib.pyplot as plt

file_path = os.path.join('graph','encoded_edges_count_window_size_5.txt')

a = open(file_path,'r')

Edges = []

while True:
	line = a.readline()
	line = line[:-1]
	line = line.split('\t')
	if line == None:
		break
	if len(line) == 3:
		Edges.append((int(line[2]),(int(line[0]),int(line[1]))))


Edges = sorted(Edges)
X = []
Y = []

for i in range(len(Edges)):
	X.append(i)
	Y.append(Edges[i][0])

plt.plot(X,Y,'ro')
plt.show()
