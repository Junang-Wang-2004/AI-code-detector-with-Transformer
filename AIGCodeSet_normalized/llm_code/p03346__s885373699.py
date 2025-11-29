import numpy as np
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = 0
for v3 in range(v1 // 2 - 1, 0, -1):
    if v2[v3] > v2[v3 + 1]:
        v2.insert(0, v2[v3])
        v2.pop(v3 + 1)
        v4 += 1
for v3 in range(v1 // 2, v1 - 1):
    if v2[v3] > v2[v3 + 1]:
        v2.append(v2[v3])
        v2.pop(v3)
        v4 += 1
print(v4)
