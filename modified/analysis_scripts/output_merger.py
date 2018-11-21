import os
import pickle

Dictionary = {}
with open("output/1_dict_merged.txt", "r") as file:
    for line in file:
        L = line[:-1]
        L = L.split('\t')
        if len(L) == 2:
            Dictionary[L[0]] = int(L[1])
            
Edges = {}
with open("output/1_graph.txt", "r") as file:
    for line in file:
        L = line[:-1]
        L = L.split('\t')
        if len(L) == 3:
            Edges[(int(L[0]),int(L[1]))] = int(L[2])  


for i in range(2,25):
    
    print(i)
    
    Id2Id = {}
    with open("output/" + str(i) + "_dict_merged.txt", "r") as file:
        for line in file:
            L = line[:-1]
            L = L.split('\t')
            if len(L) == 2:
                if L[0] in Dictionary:
                    Id2Id[int(L[1])] = Dictionary[L[0]]
                else:
                    Id2Id[int(L[1])] = len(Dictionary)
    
    print('Dictionary done!')

    with open("output/" + str(i) + "_graph.txt", "r") as file:
    for line in file:
        L = line[:-1]
        L = L.split('\t')
        if len(L) == 3:
            a = int(L[0])
            b = int(L[1])
            c = int(L[2])
            if (a,b) in Edges:
                Edges[(a,b)] += c
            else:
                Edges[(a,b)] = c

    print('Graph done!')

    with open('dict' + str(i) + '.txt', 'wb') as handle:
        pickle.dump(Dictionary,handle)

    with open('graph' + str(i) + '.txt', 'wb') as handle:
        pickle.dump(Edges,handle)

    print('Dumping done!')
