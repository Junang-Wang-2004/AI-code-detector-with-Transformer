import numpy as np
v1, v2 = map(int, input().split())
v3 = np.zeros([v2, v1 - 1])
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v4, min(v5, v6) - 1:max(v5, v6) - 1] += 1
v7 = 0
while v3.sum() != 0:
    v8 = v3.sum(axis=0)
    v3[np.argmax(v8), :] = 0
    v7 += 1
print(v7)
