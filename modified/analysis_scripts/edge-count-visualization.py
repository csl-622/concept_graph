import matplotlib.pyplot as plt
import math

A = []
B = []
with open("graph.txt", "r") as file:
    c = 0
    for line in file:
        c += 1
        if c > 100000:
            break
        L = line[:-1]
        L = L.split('\t')
        if len(L) == 3:
            A.append(math.log(int(L[2])))
            B.append(math.log(c))
        else:
            break

plt.xlabel('log of index')
plt.ylabel('log of count')
plt.plot(B,A,'b-')
plt.show()
