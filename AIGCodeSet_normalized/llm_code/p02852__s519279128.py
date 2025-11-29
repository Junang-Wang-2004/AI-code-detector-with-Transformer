v1, v2 = [int(s) for v3 in input().split()]
v3 = [int(v3) for v3 in input()]
v4 = [None] * (v1 + 1)
v5 = 0
for v6 in range(1, v1 + 1):
    if v3[v6]:
        continue
    v5 = max(v5, v6 - v2)
    while v3[v5]:
        v5 += 1
        if v5 >= v6:
            break
    if v5 < v6:
        v4[v6] = v5
if v4[v1] is None:
    print(-1)
else:
    v7 = []
    v8 = v1
    while True:
        v9 = v8 - v4[v8]
        v7.append(v9)
        v8 = v4[v8]
        if v8 == 0:
            break
    print(' '.join((str(v3) for v3 in v7[::-1])))
