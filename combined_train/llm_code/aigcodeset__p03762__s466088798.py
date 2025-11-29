import numpy as np
from numpy import array, matrix
v1, v2 = [int(n) for v3 in input().split()]
v4 = array([int(v3) for v3 in input().split()])
v5 = array([int(v3) for v3 in input().split()])
v6 = v4[1:v1] - v4[0:v1 - 1]
v7 = v5[1:v2] - v5[0:v2 - 1]
v8 = np.zeros(int(v1 * (v1 - 1) / 2))
v9 = np.zeros(int(v2 * (v2 - 1) / 2))
v10 = np.zeros(v1)
v11 = np.zeros(v2)
for v3 in range(v1 - 1):
    v10 += array([v6[v3]] * (v3 + 1) + [0] * (v1 - v3 - 2))
    v8[int(v3 * (v3 + 1) / 2):int((v3 + 1) * (v3 + 2) / 2) - 1] = v10[0:v3 + 1]
for v12 in range(v2 - 1):
    v11 += array([v7[v12]] * (v12 + 1) + [0] * (v2 - v12 - 2))
    v9[int(v12 * (v12 + 1) / 2):int((v12 + 1) * (v12 + 2) / 2) - 1] = v11[0:v12 + 1]
v13 = matrix(v8)
v14 = matrix(v9)
print(int((v14.T @ v13).sum() % (10 ** 9 + 7)))
