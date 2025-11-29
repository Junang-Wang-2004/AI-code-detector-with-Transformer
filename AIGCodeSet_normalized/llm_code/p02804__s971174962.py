def f1(a1, a2, a3):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return g1[a1] * g2[a2] * g2[a1 - a2] % a3
v1 = 10 ** 5
v2 = 10 ** 9 + 7
v3 = [1, 1]
v4 = [1, 1]
v5 = [0, 1]
for v6 in range(2, v1 + 1):
    v3.append(v3[-1] * v6 % v2)
    v5.append(-v5[v2 % v6] * (v2 // v6) % v2)
    v4.append(v4[-1] * v5[-1] % v2)
v1, v7 = map(int, input().split())
v8 = list(map(int, input().split()))
v8.sort()
v9 = 10 ** 9 + 7
v10 = 0
v11 = 0
for v6, v12 in enumerate(v8):
    v10 += f1(v6, v7 - 1, v9) * v12
    v10 %= v9
    v11 += f1(v1 - v6 - 1, v7 - 1, v9) * v12
    v11 %= v9
v13 = (v10 - v11) % v9
print(v13)
