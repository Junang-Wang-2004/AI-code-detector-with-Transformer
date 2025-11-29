v1, v2 = map(int, input().split())
v3 = []
v4 = 10 ** 6
for v5 in range(v1):
    v3.append(v4)
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v3[v6 - 1] = min(v7 - 1, v3[v6 - 1])
v8 = v4
v9 = 0
for v5 in range(v1):
    if v3[v5] == v4:
        pass
    elif v5 >= v8:
        v9 = v9 + 1
        v8 = v3[v5]
    else:
        v8 = min(v8, v3[v5])
print(v9 + 1)
