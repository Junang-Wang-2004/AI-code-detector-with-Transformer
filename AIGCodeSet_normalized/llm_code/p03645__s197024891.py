import sys
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5 = list(map(int, input().strip().split(' ')))
    v3.append(v5)
v6 = []
v7 = []
for v8 in v3:
    if v8[0] == 1:
        v6.append(v8[1])
    if v8[1] == v1:
        v7.append(v8[0])
v6.sort()
for v9 in v6:
    if v9 in v7:
        print('POSSIBLE')
        sys.exit()
print('IMPOSSIBLE')
