import sys
input = sys.stdin.readline
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in [0] * v1]
v4 = {(i, j): 0 for v5 in range(v1) for v6 in range(v5 + 1, v1)}
v7 = {(v5, v6): [] for v5 in range(v1) for v6 in range(v5 + 1, v1)}
for v5, v8 in enumerate(v2):
    v9 = (0, v8[0] - 1)
    for v6 in range(v1 - 2):
        v10 = v8[v6 + 1] - 1
        v11 = v9
        v9 = (v6, v10) if v6 < v10 else (v10, v6)
        v7[v11].append(v9)
        v4[v9] += 1
v12 = [k for v13 in v4 if v4[v13] == 0]
v14 = 0
v15 = 0
while v12:
    v16 = []
    for v13 in v12:
        for v17 in v7[v13]:
            v4[v17] -= 1
            v15 += 1
            if v4[v17] == 0:
                v16.append(v17)
    v14 += 1
    v12 = v16
if v15 != v1 * (v1 - 2):
    v14 = -1
print(v14)
