def f1(a1, a2, a3, a4):
    v1 = 0
    for v2 in range(1, a1 + 1):
        for v3 in range(v2 + 1, a1 + 1):
            for v4 in range(1, a2 + 1):
                v5 = 0
                for v6, v7, v8, v9 in a4:
                    if v6 == v2 and v7 == v3 and (v4 - v2 == v8):
                        v5 += v9
                v1 = max(v1, v5)
    return v1
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v3):
    v6, v7, v8, v9 = map(int, input().split())
    v4.append((v6, v7, v8, v9))
print(f1(v1, v2, v3, v4))
