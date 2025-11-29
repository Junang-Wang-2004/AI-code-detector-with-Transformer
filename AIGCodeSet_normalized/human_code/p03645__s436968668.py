import sys
v1, v2 = list(map(int, input().split()))
v3 = set()
v4 = [False] * (v1 + 1)
for v5 in range(v2):
    v6, v7 = list(map(int, input().split()))
    if v6 == 1:
        v3.add(v7)
    elif v7 == v1:
        v4[v6] = True
for v8 in v3:
    if v4[v8]:
        print('POSSIBLE')
        sys.exit()
print('IMPOSSIBLE')
