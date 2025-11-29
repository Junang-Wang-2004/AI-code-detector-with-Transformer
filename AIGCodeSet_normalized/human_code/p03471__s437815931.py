v1, v2 = map(int, input().split())
v3 = v2
v4 = False
for v5 in range(v3 // 10000 + 1):
    v3 = v2 - 10000 * v5
    if v5 + v3 // 1000 < v1:
        continue
    for v6 in range(v3 // 5000 + 1):
        v7 = v3 - 5000 * v6
        v8 = v7 // 1000
        if v5 + v6 + v8 == v1:
            print('{} {} {}'.format(v5, v6, v8))
            v4 = True
            break
    if v4:
        break
if not v4:
    print('-1 -1 -1')
