v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1 + 1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5].append(v6)
    v3[v6].append(v5)
for v7 in v3[1]:
    for v8 in v3[v7]:
        if v8 == v1:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')
