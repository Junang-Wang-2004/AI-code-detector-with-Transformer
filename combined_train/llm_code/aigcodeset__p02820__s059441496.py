v1, v2 = map(int, input().split())
v3, v4, v5 = map(int, input().split())
v6 = input()
v7 = {'r': v5, 's': v3, 'p': v4}
v8 = {'r': 'p', 's': 'r', 'p': 's'}
v9 = {'r': 's', 's': 'p', 'p': 'r'}
v10 = []
v11 = 0
for v12 in range(v1):
    if len(v10) < v2:
        v11 += v7[v6[v12]]
        v10.append(v8[v6[v12]])
    elif v8[v6[v12]] != v10[-v2]:
        v11 += v7[v6[v12]]
        v10.append(v8[v6[v12]])
    elif v6[v12] != v10[-v2]:
        v10.append(v6[v12])
    else:
        v10.append(v9[v6[v12]])
print(v11)
