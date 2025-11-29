def f1(a1, a2, a3):
    return fac[a1] * facinv[a2] * facinv[a1 - a2] % a3

def f2(a1, a2):
    for v1 in range(2, a1 + 1):
        fac.append(fac[v1 - 1] * v1 % a2)
        inv.append(-inv[a2 % v1] * (a2 // v1) % a2)
        facinv.append(facinv[-1] * inv[-1] % a2)
v1 = [1, 1]
v2 = [1, 1]
v3 = [0, 1]
v4 = int(input())
v5 = input()
v6 = len(v5)
v7 = 1000000007
f2(v6 + v4 - 1, v7)
v8 = 0
for v9 in range(v4 + 1):
    v10 = pow(25, v4 - v9, v7)
    v10 *= f1(v6 + v4 - v9 - 1, v4 - v9, v7)
    v10 %= v7
    v10 *= pow(26, v9, v7)
    v10 %= v7
    v8 += v10
    v8 %= v7
print(v8)
