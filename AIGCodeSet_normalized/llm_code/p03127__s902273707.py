import numpy as np
v1 = int(input())
v2 = np.array([int(i) for v3 in input().split()])
v2 = np.sort(v2)
v4 = v2[0]
for v3 in range(max([v1, v4])):
    v5 = v2[0]
    v2 = v2 % v5
    v2[0] = v5
    v6 = np.count_nonzero(v2)
    v2 = np.sort(v2)[v6:]
    for v7 in range(len(v2)):
        if v2[0] != 0:
            break
        v2 = np.delete(v2, 0)
    if len(v2) == 1:
        break
print(v2[0])
