import numpy as np
v1, v2, v3, v4, v5 = map(int, input().split())
v6 = sorted(list(map(int, input().split())))
v7 = sorted(list(map(int, input().split())))
v8 = sorted(list(map(int, input().split())))
v9 = v6[-v1:]
v10 = v7[-v2:]
v9.extend(v10)
v9.extend(v8)
v11 = sorted(v9)
v12 = np.sum(np.array(v11)[-v1 - v2:])
print(str(v12))
