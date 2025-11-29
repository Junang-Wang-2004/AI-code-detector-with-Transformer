v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1 - 1)]
v4 = list(map(int, input().split()))
v4.sort()
v5 = sum(v4[:-1])
v6 = {}
for v7, v8 in v2:
    v6.setdefault(v7, set()).add(v8)
    v6.setdefault(v8, set()).add(v7)
v9 = []
v10 = [0] * (v1 + 1)
for v11, v12 in v6.items():
    v10[v11] = len(v12)
    if len(v12) == 1:
        v9.append(v11)
v13 = v9.copy()
v14 = [0] * (v1 + 1)
for v15 in v13:
    v14[v15] = 1
v16 = v9.copy()
while v16:
    v17 = []
    for v12 in v16:
        for v18 in v6[v12]:
            v10[v18] -= 1
            if v14[v18] == 0:
                v14[v18] = 1
                v13.append(v18)
                v17.append(v18)
    v16 = [v12 for v12 in v17 if v10[v12] == 0]
v19 = [0] * v1
for v20 in range(v1):
    v19[v13[v20] - 1] = v4[v20]
print(v5)
print(*v19)
