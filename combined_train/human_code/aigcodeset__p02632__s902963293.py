v1 = int(input())
v2 = input()
v3 = len(v2)
v4 = 10 ** 9 + 7
v5 = 10 ** 7
v6 = [1]
v7 = [0] * (v5 + 4)
for v8 in range(v5 + 3):
    v6.append(v6[-1] * (v8 + 1) % v4)
v7[-1] = pow(v6[-1], v4 - 2, v4)
for v8 in range(v5 + 2, -1, -1):
    v7[v8] = v7[v8 + 1] * (v8 + 1) % v4

def f1(a1, a2, a3):
    return v6[a1] * v7[a2] % a3 * v7[a1 - a2] % a3
v9 = 0
for v8 in range(v1 + 1):
    v10 = pow(26, v8, v4) * pow(25, v1 - v8, v4) * f1(v1 + v3 - v8 - 1, v3 - 1, v4)
    v10 %= v4
    v9 += v10
    v9 %= v4
print(v9)
