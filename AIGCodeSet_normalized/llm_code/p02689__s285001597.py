v1, v2 = [int(_) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = [set() for v6 in range(v1)]
v7 = 0
for v6 in range(v2):
    v6, v8 = [int(v3) for v3 in input().split()]
    v5[v6 - 1].add(v8 - 1)
    v5[v8 - 1].add(v6 - 1)
for v9, v10 in enumerate(v5):
    v11 = 1
    for v6 in v10:
        if v4[v6] >= v4[v9]:
            v11 = 0
            break
    if v11 == 1:
        v7 += 1
print(v7)
