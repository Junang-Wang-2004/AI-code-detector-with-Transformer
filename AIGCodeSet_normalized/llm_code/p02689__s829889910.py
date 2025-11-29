v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [[] for v5 in range(v1)]
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v6 -= 1
    v7 -= 1
    v4[v6].append(v3[v7])
    v4[v7].append(v3[v6])
v8 = 0
for v9 in range(v1):
    if not v4[v9] or all((v3[v9] > h for v10 in v4[v9])):
        v8 += 1
print(v8)
