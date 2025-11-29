import numpy as np
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(list(map(int, input().split())))
v6 = np.array(v4)
if np.sum(v6, axis=0)[1:] < v3:
    print(-1)
    exit()
else:
    for v7 in v6:
        pass
