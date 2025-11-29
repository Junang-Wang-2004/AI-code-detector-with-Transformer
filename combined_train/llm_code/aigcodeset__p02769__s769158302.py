def f1(a1, a2, a3):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return g1[a1] * g2[a2] * g2[a1 - a2] % a3
v1 = 10 ** 9 + 7
v2 = 10 ** 6
v3 = [1, 1]
v4 = [1, 1]
v5 = [0, 1]
for v6 in range(2, v2 + 1):
    v3.append(v3[-1] * v6 % v1)
    v5.append(-v5[v1 % v6] * (v1 // v6) % v1)
    v4.append(v4[-1] * v5[-1] % v1)
v2, v7 = map(int, input().split())
v8 = 10 ** 9 + 7
v9 = max(v2, v7)
v10 = 0
for v6 in range(max(1, v2 - v9), v2 + 1):
    v11 = f1(v2, v6, v8)
    v11 *= f1(v2 - 1, v6 - 1, v8)
    v10 += v11
    v10 %= v8
print(v10)
