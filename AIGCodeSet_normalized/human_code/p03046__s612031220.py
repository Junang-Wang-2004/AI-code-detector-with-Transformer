def f1(a1, a2):
    v1 = 2 ** a1
    if a2 > v1 - 1:
        return [-1]
    if a2 == 0:
        v2 = []
        for v3 in range(v1):
            v2.append(v3)
            v2.append(v3)
        return v2
    if a1 == 1:
        return [-1]
    v4 = [False] * v1
    v4[0] = True
    v4[a2] = True
    v5 = []
    for v3 in range(1, v1):
        if v4[v3]:
            continue
        v5.append([v3, a2 ^ v3])
        v4[v3] = True
        v4[a2 ^ v3] = True
    v6 = []
    for v7, v8 in v5:
        v6.append(v7)
        v6.append(v8)
    v2 = v6 + [0, a2, 0] + v6[::-1] + [a2]
    return v2
v1, v2 = map(int, input().split())
v3 = f1(v1, v2)
print(*v3)
