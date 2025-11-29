v1, v2, v3 = map(int, input().split())
v4 = [0] * v1
v5 = [0] * v2
v6 = set()
for v7 in range(v3):
    v8, v9 = map(int, input().split())
    v4[v8 - 1] += 1
    v5[v9 - 1] += 1
    v6.add((v8 - 1, v9 - 1))
v10 = max(v4)
v11 = max(v5)
v12 = [v7 for v7, v13 in enumerate(v4) if v13 == v10]
v14 = [v7 for v7, v13 in enumerate(v5) if v13 == v11]
import sys
for v7 in v12:
    for v15 in v14:
        if (v7, v15) not in v6:
            print(v10 + v11)
            sys.exit()
print(v10 + v11 - 1)
