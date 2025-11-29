def f1():
    return [int(j) for v1 in input().split()]
v1, v2 = f1()
v3 = [[] for v4 in range(v1 + 1)]
for v5 in range(v1 - 1):
    v6, v7 = f1()
    v3[v6].append(v7)
    v3[v7].append(v6)
v8 = [0 for v4 in range(v1 + 1)]
for v5 in range(v2):
    v9, v10 = f1()
    v8[v9] += v10
for v5 in range(1, v1 + 1):
    for v10 in v3[v5]:
        if v5 > v10:
            continue
        v8[v10] += v8[v5]
print(*v8[1:])
