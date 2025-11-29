v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = False
for v6 in range(v2):
    for v7 in range(v2):
        if v3[v6][1] == v3[v7][0] and v3[v7][1] == v1:
            v5 = True
            break
if v5:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
