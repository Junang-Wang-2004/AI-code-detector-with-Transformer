import numpy as np
v1 = input()
v2 = input().strip().split()
v3 = [0] * 100000
v4 = [0] * 100000
v5 = v2[0::2]
v6 = v2[1::2]
for v7 in v5:
    v7 = int(v7)
    v3[v7] = v3[v7] + 1
for v8 in v6:
    v8 = int(v8)
    v4[v8] = v4[v8] + 1
print(len(v5) - int(max(v3)) + len(v6) - int(max(v4)))
