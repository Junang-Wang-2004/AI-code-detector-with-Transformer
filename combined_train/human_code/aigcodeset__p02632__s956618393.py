import sys
v1 = sys.stdin.readline
v2 = int(v1())
v3 = v1().rstrip()
v3 = len(v3)
v4 = v2 + v3
v5 = 10 ** 9 + 7
v6 = 10 ** 6 * 2
v7 = [1] * 2 + [0] * (v6 - 2)
v8 = [1] * 2 + [0] * (v6 - 2)
v9 = [0, 1] + [0] * (v6 - 2)
for v10 in range(2, v6):
    v7[v10] = v7[v10 - 1] * v10 % v5
    v9[v10] = -v9[v5 % v10] * (v5 // v10) % v5
    v8[v10] = v8[v10 - 1] * v9[v10] % v5

def f1(a1, a2, a3):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return v7[a1] * v8[a2] * v8[a1 - a2] % a3
v11 = 0
for v12 in range(v3, v4 + 1):
    v13 = f1(v12 - 1, v3 - 1, v5)
    v13 *= pow(25, v12 - v3, v5)
    v13 %= v5
    v13 *= pow(26, v4 - v12, v5)
    v13 %= v5
    v11 += v13
    v11 %= v5
print(v11)
