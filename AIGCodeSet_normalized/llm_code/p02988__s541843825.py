import numpy as np
v1 = input()
v2 = input()
v3 = np.array(v2.split(' '), dtype=np.int32)
v3 = np.sort(v3)
v4 = int(len(v3) / 2) + 1
print(v3[v4] - v3[v4 - 1])
