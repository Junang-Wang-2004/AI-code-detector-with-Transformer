v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1 + 1)]
v5 = [-1 if i == 1 else None for v6 in range(v1 + 1)]
v7 = [0 for v6 in range(v1 + 1)]
for v4 in range(v1 - 1):
    v8, v9 = map(int, input().split())
    v3[v8].append(v9)
    v5[v9] = v8
for v4 in range(v2):
    v10, v11 = map(int, input().split())
    v7[v10] += v11
v12 = [1]
while v12:
    v13 = v12.pop()
    if v3[v13]:
        for v14 in v3[v13]:
            v7[v14] += v7[v13]
            v12.append(v14)
print(' '.join([str(num) for v15 in v7[1:v1 + 1]]))
