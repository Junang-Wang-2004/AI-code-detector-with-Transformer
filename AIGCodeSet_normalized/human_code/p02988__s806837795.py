import numpy as np
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [x for v4 in range(1, v1 - 1)]
v5 = 0
for v6 in v3:
    v7 = np.sort([v2[v6 - 1], v2[v6], v2[v6 + 1]])
    v5 = v5 + 1 if v7[1] == v2[v6] else v5
print(v5)
