import sys
input = sys.stdin.readline
from scipy.optimize import linear_sum_assignment
import numpy as np
v1 = int(input())
v2 = [[int(x) for v3 in input().split()] for v4 in range(v1)]
v5 = [[int(v3) for v3 in input().split()] for v4 in range(v1)]
v6 = np.zeros((v1, v1), dtype=np.int32)
for v7, (v8, v9) in enumerate(v2):
    for v10, (v11, v12) in enumerate(v5):
        if v8 < v11 and v9 < v12:
            v6[v7, v10] = 1
v13, v14 = linear_sum_assignment(v6, maximize=True)
v15 = v6[v13, v14].sum()
print(v15)
