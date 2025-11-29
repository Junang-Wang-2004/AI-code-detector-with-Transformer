import sys
v1, v2, v3 = map(int, input().split())
v4 = [0] * v1
v5 = [0] * v2
v6 = [[0] * v2 for v7 in [1] * v1]
for v7 in range(v3):
    v8, v9 = map(int, input().split())
    v4[v8 - 1] += 1
    v5[v9 - 1] += 1
    v6[v8 - 1][v9 - 1] = 1
v10 = max(v4)
v11 = max(v5)
v12 = [n for v13, v14 in enumerate(v4) if v14 == v10]
v15 = [v13 for v13, v14 in enumerate(v5) if v14 == v11]
v16 = 0
for v8 in v12:
    for v9 in v15:
        if v6[v8][v9] == 0:
            print(v10 + v11)
            v16 = 1
            sys.exit()
if v16 == 0:
    print(v10 + v11 - 1)
