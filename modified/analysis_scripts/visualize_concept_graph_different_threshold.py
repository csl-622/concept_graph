import networkx as nx
import os

A = sorted(os.listdir('pickles'))
N = []
X = []
Y = []
Z = []
c = 0
for i in A:
    print(i)
    c += 1
    G = nx.read_gpickle(os.path.join('pickles',i))
    n = G.number_of_nodes()
    m = G.number_of_edges()
    N.append(i)
    X.append(c)
    Y.append(n)
    Z.append(m)

print(N)
print(X)
print(Y)
print(Z)
