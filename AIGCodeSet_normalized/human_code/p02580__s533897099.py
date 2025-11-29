import sys
from itertools import product
v1, v2, v3 = map(int, input().split())
v4 = [0 for v5 in range(v1)]
v6 = [0 for v5 in range(v2)]
v7 = set()
for v5 in range(v3):
    v8, v9 = map(int, input().split())
    v8, v9 = (v8 - 1, v9 - 1)
    v7.add((v8, v9))
    v4[v8] += 1
    v6[v9] += 1
v10 = max(v4)
v11 = max(v6)
v12 = []
for v5 in range(v1):
    if v4[v5] == v10:
        v12.append(v5)
v13 = []
for v5 in range(v2):
    if v6[v5] == v11:
        v13.append(v5)
for v14 in v12:
    for v15 in v13:
        if (v14, v15) not in v7:
            print(v10 + v11)
            sys.exit()
print(v10 + v11 - 1)
