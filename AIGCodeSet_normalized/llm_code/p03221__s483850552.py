def f1(a1, a2):
    v1 = len(a1)
    v2 = 0
    v3 = v1
    while v2 != v3:
        if a2 > a1[(v2 + v3) // 2]:
            v2 = (v2 + v3) // 2 + 1
        else:
            v3 = (v2 + v3) // 2
    return v2
v1, v2 = map(int, input().split())
v3 = []
v4 = []
v5 = [[] for v6 in range(v1)]
for v7 in range(v2):
    v8, v9 = map(int, input().split())
    v3.append(v8)
    v4.append(v9)
    v5[v8 - 1].append(v9)
for v7 in range(v1):
    v5[v7].sort()
for v7 in range(v2):
    v10 = f1(v5[v3[v7] - 1], v4[v7]) + 1
    print('%06d%06d' % (v3[v7], v10))
