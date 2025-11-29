import numpy as np
v1, v2 = [int(i) for v3 in input().split()]
v4 = np.array([], dtype=np.int64)
if v2 - v1 >= 0:
    v4 = np.append(v4, v2 - v1)
if v2 + v1 >= 0:
    v4 = np.append(v4, v2 + v1 + 1)
if -v2 - v1 >= 0:
    v4 = np.append(v4, -v2 - v1 + 1)
if -v2 + v1 >= 0:
    v4 = np.append(v4, -v2 + v1 + 2)
print(v4.min())
