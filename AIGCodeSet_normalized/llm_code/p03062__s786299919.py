from sys import stdin
import numpy as np
v1 = int(stdin.readline().rstrip())
v2 = [int(x) for v3 in stdin.readline().rstrip().split()]
v2 = np.array(v2)
v4 = 0
v5 = 0
for v6 in v2[v2 > 0]:
    v4 += v6
for v7 in v2[v2 < 0][0:-1]:
    v4 += abs(v7)
if len(v2[v2 < 0]) % 2 == 0:
    v4 += abs(v2[v2 < 0][-1])
print(v4)
