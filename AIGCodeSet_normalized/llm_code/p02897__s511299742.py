import numpy as np
v1 = int(input())
v2 = list(map(int, input().split()))
v2 = np.array(v2)
v3 = np.array(range(v1))
v4 = np.vstack([v2, v3])
v4 = v4[:, v4[0, :].argsort()]
v5 = v4[1, :] + 1
v5 = str(v5)
print(v5)
