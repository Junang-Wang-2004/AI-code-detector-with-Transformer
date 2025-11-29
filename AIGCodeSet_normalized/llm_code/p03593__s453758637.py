v1, v2, v3 = open(0).read().partition('\n')
v4, v5 = map(int, v1.split())
v6 = {}
v6[3] = v4 // 2 * (v5 // 2)
v6[0] = v4 % 2 and v5 % 2
v6[1] = (v4 * v5 - v6[3] * 4 - v6[0]) // 2
for v7 in set(v3) - {'\n'}:
    v7 = v3.count(v7)
    for v8 in [3, 1, 0]:
        while v6[v8] and v7 > v8:
            v7 -= v8 + 1
            v6[v8] -= 1
print('YNeos'[any((v1 for v1 in v6.values()))::2])
