v1 = input()
v2 = 10 ** 9 + 7
v3 = len(v1)
v4 = [0] * (v3 + 1)
v5 = [0] * (v3 + 1)
v4[0] = 1
for v6 in range(v3):
    if v1[v6] == '1':
        v4[v6 + 1] += v4[v6] * 2
        v4[v6 + 1] %= v2
        v5[v6 + 1] += v4[v6] + v5[v6] * 3
        v5[v6 + 1] %= v2
    else:
        v4[v6 + 1] += v4[v6]
        v4[v6 + 1] %= v2
        v5[v6 + 1] += v5[v6] * 3
        v5[v6 + 1] %= v2
print((v4[v3] + v5[v3]) % v2)
