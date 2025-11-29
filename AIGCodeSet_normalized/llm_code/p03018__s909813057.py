from sys import stdin
import numpy as np
v1 = stdin.readline().rstrip().split()[0]
v2 = len(v1)
v3 = []
v4 = 0
while v4 < v2:
    if v4 > v2 - 2:
        v3.append(v1[v4])
        v4 += 1
    elif v1[v4:v4 + 2] == 'BC':
        v3.append('E')
        v4 += 2
    elif v4 > v2 - 3:
        v3.append(v1[v4])
        v4 += 1
    elif v1[v4:v4 + 3] == 'ABC':
        v3.append('D')
        v4 += 3
    else:
        v3.append(v1[v4])
        v4 += 1
v5 = len(v3)
v6 = 0
for v4 in range(v5 - 1):
    if v3[v4] == 'A' and v3[v4 + 1] == 'D':
        v3[v4] = 'D'
        v3[v4 + 1] = 'A'
        v6 += 1
        if v4 < v5 - 4:
            if v3[v4 + 3] == 'E':
                v3[v4] = 'D'
                del v3[v4 + 3]
v5 = len(v3)
for v4 in range(v5 - 1):
    if v3[v5 - 1 - v4] == 'E' and v3[v5 - 2 - v4] == 'D':
        v3[v5 - 1 - v4] = 'D'
        v3[v5 - 2 - v4] = 'E'
        v6 += 1
v3.append('Z')
v7 = 0
v8 = 0
for v4 in range(v5 + 1):
    if v3[v4] == 'D':
        v7 += 1
    else:
        if v7 != 0:
            v6 += v7 * (v7 + 1) // 2
        v7 = 0
print(v6)
