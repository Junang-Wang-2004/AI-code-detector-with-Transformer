from scipy.special import comb
v1, v2 = map(int, input().split())
v3 = [int(x) for v4 in input().split()]
v3.sort()
v5 = 0
v6 = 10 ** 9 + 7
v7 = dict()
for v8 in range(v2 - 2, v1):
    v7[v8] = int(comb(v8, v2 - 2)) % v6
for v9 in range(v1):
    for v10 in range(v1):
        if v1 - v9 - v10 >= v2:
            v5 += int((v3[v1 - 1 - v10] - v3[v9]) * v7[v1 - v10 - 2 - v9] % v6)
        if v1 - 1 - v10 < v9:
            break
print(v5 % v6)
