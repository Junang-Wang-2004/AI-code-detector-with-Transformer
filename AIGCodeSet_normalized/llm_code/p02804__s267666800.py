from scipy.misc import comb
v1, v2 = map(int, input().split())
v3 = [int(x) for v4 in input().split()]
v3 = sorted(v3)
v5 = 10 ** 9 + 7
v6 = [0] * v1
v7 = [0] * v1
v8 = 0
v9 = comb(v1 - 1, v2 - 1, exact=True) % v5
v8 += v9 * v3[v1 - 1] % v5
v8 -= v9 * v3[0] % v5
v8 = v8 % v5
for v10 in range(1, v1):
    if v1 - v10 >= v2:
        if v1 - v10 == 1:
            v9 = 1
        else:
            v9 = comb(v1 - v10 - 1, v2 - 1, exact=True) % v5
        v8 += v9 * v3[v1 - v10 - 1] % v5
        v8 -= v9 * v3[v10] % v5
        v8 = v8 % v5
print(v8)
