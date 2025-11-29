v1, v2 = map(int, input().split())
v3 = set()
v4 = set()
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    if v6 == 1:
        v4.add(v7)
    if v7 == v1:
        v3.add(v6)
print('POSSIBLE' if len(v3 & v4) > 0 else 'IMPOSSIBLE')
