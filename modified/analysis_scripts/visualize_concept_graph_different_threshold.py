import networkx as nx
import matplotlib.pyplot as plt
import os
def fun(s):
    ans = 0
    S = list(s)
    for i in S:
        if ord(i) - ord('0') >= 0 and ord(i) - ord('9') <= 0:
            ans *= 10
            ans += int(i)
    return ans

L = sorted(os.listdir('pickles'))
A = []
for i in L:
    A.append((fun(i),i))

A = sorted(A)    
   
X = []
Nodes = []
Edges = []
for i in A:
    G = nx.read_gpickle(os.path.join('pickles',i[1]))
    n = G.number_of_nodes()
    m = G.number_of_edges()
    Nodes.append(n)
    Edges.append(m)
    X.append(i[0])

plt.plot(X,Y,'r^')
plt.show()

plt.plot(X,Z,'g^')
plt.show()
