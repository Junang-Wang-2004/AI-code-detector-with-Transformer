import numpy as np
v1, v2 = list(map(int, input().split()))
v3 = []
v4 = np.array([])
for v5 in range(v1):
    v3 = list(map(int, input().split()))
    v4 = np.concatenate((v4, v3[0] * np.ones(v3[1])))
v4 = np.sort(v4)
print(int(v4[v2 - 1]))
