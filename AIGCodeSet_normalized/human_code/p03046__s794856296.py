v1, v2 = map(int, input().split())
if v2 >= 2 ** v1:
    print(-1)
    exit()
if v1 == 1:
    if v2 == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    exit()
v3 = [0 for v4 in range(2 ** (v1 + 1))]
for v5 in range(2 ** v1):
    if v5 < v2:
        v3[v5] = v5
        v3[2 ** (v1 + 1) - 2 - v5] = v5
    if v5 == v2:
        continue
    if v5 > v2:
        v3[v5 - 1] = v5
        v3[2 ** (v1 + 1) - v5 - 1] = v5
v3[2 ** v1 - 1] = v2
v3[2 ** (v1 + 1) - 1] = v2
print(*v3, sep=' ')
