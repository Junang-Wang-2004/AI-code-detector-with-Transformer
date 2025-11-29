v1, v2 = map(int, input().split(' '))
v3 = [tuple(map(int, input().split(' '))) for v4 in range(v2)]
v5, v6 = (set(), set())
for v7 in v3:
    if v7[0] == 1:
        v5.add(v7[1])
    if v7[1] == v1:
        v6.add(v7[0])
print('POSSIBLE' if v5 & v6 else 'IMPOSSIBLE')
