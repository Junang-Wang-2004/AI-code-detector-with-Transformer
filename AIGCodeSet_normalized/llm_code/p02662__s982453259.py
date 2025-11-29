class C1:

    def __init__(a1, a2):
        a1.MOD = a2

    def modpow(a1, a2, a3):
        v1 = 1
        while a3 > 0:
            if a3 & 1:
                v1 = v1 * a2 % a1.MOD
            a2 = a2 * a2 % a1.MOD
            a3 >>= 1
        return v1

    def invx(a1, a2):
        return a1.modpow(a2, a1.MOD - 2)

    def invpowL(a1, a2, a3):
        v1 = a1.invx(a2)
        v2 = [1] * (a3 + 1)
        for v3 in range(1, a3 + 1):
            v2[v3] = v2[v3 - 1] * v1 % a1.MOD
        return v2

    def invL(a1, a2):
        v1 = [0, 1]
        for v2 in range(2, a2 + 1):
            v1.append(a1.MOD - v1[a1.MOD % v2] * (a1.MOD // v2) % a1.MOD)
        return v1
v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = 998244353
v5 = [[0] * (v2 + 1) for v6 in range(v1 + 1)]
v7 = C1(v4)
v8 = v7.invx(2)
v9 = v7.modpow(2, v1 - 1)
for v10 in range(1, v1 + 1):
    v11 = v3[v10 - 1]
    if v11 > v2:
        for v12 in range(v2 + 1):
            v5[v10][v12] = v5[v10 - 1][v12]
    for v12 in range(v11):
        v5[v10][v12] = v5[v10 - 1][v12]
    v5[v10][v11] = (v5[v10 - 1][v11] + v9) % v4
    for v12 in range(v11 + 1, v2 + 1):
        v5[v10][v12] = (v5[v10 - 1][v12] + v5[v10 - 1][v12 - v11] * v8) % v4
for v10 in v5:
    print(v10)
print(v5[-1][v2])
