def f1(a1, a2, a3):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return g1[a1] * g2[a2] * g2[a1 - a2] % a3
v1 = 998244353
v2, v3, v4 = map(int, input().split())
v5 = [1, 1]
v6 = [1, 1]
v7 = [0, 1]
for v8 in range(2, v2):
    v5.append(v5[-1] * v8 % v1)
    v7.append(-v7[v1 % v8] * (v1 // v8) % v1)
    v6.append(v6[-1] * v7[-1] % v1)
v9 = v3 * (v3 - 1) ** (v2 - 1) % v1
for v8 in range(1, v4 + 1):
    v9 += f1(v2 - 1, v8, v1) * v3 * pow(v3 - 1, v2 - 1 - v8, v1)
    v9 %= v1
print(v9)
