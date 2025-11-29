v1, v2 = map(int, input().split())
v3 = [int(input()) for v4 in range(v2)]
'\n100 5\n1\n23\n45\n67\n89\n'
import numpy as np
import sys
v3 = np.array(v3)
v5 = v3[1:] - v3[:-1]
if 1 in v5:
    print(0)
    sys.exit()
v6 = [0] * (v1 + 3)
v6[0] = 1
v7 = 0
for v4 in range(v2):
    v8 = v3[v4]
    v9 = v8 - 1
    v10 = v9 - v7
    if v10 < 2:
        v6[v9 + 2] = v6[v7]
        v7 = v9 + 2
    else:
        v6[v7 + 1] = v6[v7]
        for v4 in range(v10 - 1):
            v6[v7 + v4 + 2] = v6[v7 + v4] + v6[v7 + v4 + 1]
        v6[v9 + 2] = v6[v9]
        v7 = v9 + 2
if v1 - v7 < 2:
    v6[v1] = v6[v7]
else:
    v10 = v1 - v7
    v6[v7 + 1] = v6[v7]
    for v4 in range(v10 - 1):
        v6[v7 + v4 + 2] = v6[v7 + v4] + v6[v7 + v4 + 1]
print(v6[v1] % 1000000007)
