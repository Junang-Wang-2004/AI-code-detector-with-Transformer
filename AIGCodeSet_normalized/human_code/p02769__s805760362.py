v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7

def f1(a1, a2, a3=10 ** 9 + 7):
    v1 = perm[a1] * inv[a2]
    v1 %= v3
    v1 *= inv[a1 - a2]
    v1 %= v3
    return v1

def f2(a1):
    return pow(a1, v3 - 2, v3)
v4 = [1] * (2 * v1 + 1)
for v5 in range(1, 2 * v1 + 1):
    v4[v5] = v4[v5 - 1] * v5
    v4[v5] %= v3
v6 = [1] * (2 * v1 + 1)
v6[-1] = f2(v4[-1])
for v5 in range(2 * v1 - 1, -1, -1):
    v6[v5] = v6[v5 + 1] * (v5 + 1)
    v6[v5] %= v3
v7 = f1(2 * v1 - 1, v1)
for v8 in range(v2 + 1, v1):
    v9 = f1(v1, v8) * f1(v1 - 1, v8)
    v9 %= v3
    v7 -= v9
    v7 %= v3
print(v7)
