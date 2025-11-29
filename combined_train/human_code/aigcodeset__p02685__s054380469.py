v1 = 998244353
v2 = 1000000
v3 = [0, 1]
v4 = [1, 1]
v5 = [1, 1]
for v6 in range(2, v2 + 1):
    v4.append(v4[-1] * v6 % v1)
    v3.append(v3[v1 % v6] * (v1 - v1 // v6) % v1)
    v5.append(v5[-1] * v3[-1] % v1)

def f1(a1, a2):
    return v4[a1] * v5[a1 - a2] % v1

def f2(a1, a2):
    return v4[a1] * v5[a1 - a2] * v5[a2] % v1

def f3(a1, a2):
    return f2(a1 + a2 - 1, a2)
v2, v7, v8 = map(int, input().split())
v9 = v7 * pow(v7 - 1, v2 - 1, v1) % v1
for v6 in range(1, v8 + 1):
    v9 += v7 * pow(v7 - 1, v2 - 1 - v6, v1) * f2(v2 - 1, v6)
    v9 %= v1
print(v9)
