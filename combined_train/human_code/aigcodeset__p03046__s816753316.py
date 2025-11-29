import sys
v1, v2 = map(int, input().strip().split())
v3 = 2 ** v1
if v2 >= v3:
    print(-1)
    sys.exit()
if v1 == 1:
    if v2 == 0:
        print('0 0 1 1')
    else:
        print('-1')
    sys.exit()
v4 = []
for v5 in range(v3):
    if v5 == v2:
        continue
    v4.append(v5)
v4.append(v2)
for v5 in range(v3):
    v6 = v3 - v5 - 1
    if v6 == v2:
        continue
    v4.append(v6)
v4.append(v2)
for v5 in range(2 ** (v1 + 1)):
    print(v4[v5], end=' ')
