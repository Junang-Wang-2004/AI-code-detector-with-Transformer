v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v3.append(tuple(map(int, input().split())))
v5 = set()
for v6, v7 in v3:
    if v6 == 1:
        v5.add(v7)
for v8 in v5:
    for v6, v7 in v3:
        if v6 == v8 and v7 == v1:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')
