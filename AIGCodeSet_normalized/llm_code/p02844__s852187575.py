v1 = int(input())
v2 = list(input())
v3 = set()
v4 = {}
v5 = set()
for v6 in range(v1):
    if v6 in v3:
        continue
    v3.add(v6)
    for v7 in range(v6 + 1, v1):
        if not v2[v7 + 1:v1] or v2[v6] + v2[v7] in v5:
            continue
        if v2[v6] + v2[v7] not in v4:
            v4[v2[v6] + v2[v7]] = set()
        v4[v2[v6] + v2[v7]].add(''.join(v2[v7 + 1:v1]))
        v5.add(v2[v6] + v2[v7])
v8 = 0
v9 = [len(value) for v10 in v4.values()]
print(sum(v9))
