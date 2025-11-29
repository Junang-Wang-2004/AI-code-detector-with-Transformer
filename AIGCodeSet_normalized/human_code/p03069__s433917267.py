from sys import stdin
import numpy as np
v1 = int(stdin.readline().rstrip().split()[0])
v2 = stdin.readline().rstrip().split()[0]
v3 = []
v4 = []
v5 = 0
v6 = 0
for v7 in range(v1):
    if v2[v7] == '.':
        v6 += 1
    v4.append(v6)
    if v2[v1 - 1 - v7] == '#':
        v5 += 1
    v3.append(v5)
v4 = np.array(v4)
v3 = np.array(v3[::-1])
v8 = v1 - np.max(v4 + v3)
print(v8)
