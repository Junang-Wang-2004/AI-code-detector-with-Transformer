v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = [[0] * (v2 + 1) for v6 in range(v1 + 1)]
for v7 in range(v2 + 1):
    v5[0][v7] = 1 if v7 == 1 else 0

def f1(a1, a2):
    assert 1 <= a1 <= v2 and 1 <= a2 <= v2
    if a1 == 1 or a2 == 1 or a1 == v2 or (a2 == v2):
        return pow(2, max(v2 - 1 - 2, 0), v4)
    else:
        return pow(2, max(v2 - 1 - 3, 0), v4)
for v8 in range(1, v1 + 1):
    for v7 in range(1, v2 + 1):
        v9 = v5[v8 - 1][v7 - 1] * f1(v7 - 1, v7) if v7 > 1 else 0
        v10 = v5[v8 - 1][v7 + 1] * f1(v7 + 1, v7) if v7 < v2 else 0
        v11 = v5[v8 - 1][v7] * (pow(2, max(v2 - 1 - 2, 0), v4) if 1 < v7 < v2 else pow(2, max(v2 - 1 - 1, 0), v4))
        v5[v8][v7] = (v9 + v10 + v11) % v4
print(v5[v1][v3])
