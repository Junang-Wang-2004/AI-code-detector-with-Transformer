v1, v2 = map(int, input().split(' '))
v3 = list(map(int, input().split(' ')))
v4 = [-1 for v5 in range(v1)]
v6 = 0
v7 = -1
v8 = 0
v9, v10 = (0, 0)
while True:
    if v4[v8] != -1:
        v7 = v8
        v10 = v6 - v4[v8]
        break
    v4[v8] = v6
    v8 = v3[v8] - 1
    v9 += 1
    v6 += 1
v11 = v9 - v10
if v2 <= v1:
    v8 = 1
    while v2 > 0:
        v2 -= 1
        v8 = v3[v8 - 1]
    print(v8)
else:
    v2 -= v11
    v2 %= v10
    v8 = v7 + 1
    while v2 > 0:
        v2 -= 1
        v8 = v3[v8 - 1]
    print(v8)
