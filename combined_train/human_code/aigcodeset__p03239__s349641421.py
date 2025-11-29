"""
B - Time Limit Exceeded
"""
import numpy as np
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5 = []
    for v6 in input().split():
        v5.append(int(v6))
    v3.append(v5)
v7 = np.array(v3)
v8 = np.argsort(v7[:, 1])
v9 = 1001
for v10 in v7[v8]:
    if v10[1] <= v2:
        v9 = min(v9, v10[0])
if v9 == 1001:
    print('TLE')
else:
    print(v9)
