import numpy as np
import sys
v1, v2 = map(int, input().split())
v3 = sorted(map(int, input().split()))
v4 = 10 ** 9 + 7
if len([a for v5 in v3[:v2] if np.sign(v5) == -1]) % 2 != 0:
    v6 = [num for v7 in v3[:v2] if np.sign(v7) == -1]
    v8 = [v7 for v7 in v3[:v2] if np.sign(v7) != 1]
    v9 = [v7 for v7 in v3[v2:] if np.sign(v7) == -1]
    v10 = [v7 for v7 in v3[v2:] if np.sign(v7) != -1]
    if len(v6) == 0 or len(v10) == 0:
        v11 = min(v8)
        v12 = min(v9)
    elif len(v8) == 0 or len(v9) == 0:
        v11 = max(v6)
        v12 = max(v10)
    else:
        v13 = max(v10)
        v14 = max(v6)
        v15 = min(v9)
        v16 = min(v8)
        if v13 / v14 < v15 / v16:
            v11 = v14
            v12 = v13
        else:
            v11 = v16
            v12 = v15
v17 = 1
for v7 in v3[:v2]:
    v17 *= v7
    v17 %= v4
if len([v5 for v5 in v3[:v2] if np.sign(v5) == -1]) % 2 != 0:
    v17 *= v12
    v17 %= v4
    v17 *= pow(v11, v4 - 2, v4)
    v17 %= v4
print(v17)
