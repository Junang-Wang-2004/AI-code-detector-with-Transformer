v1 = input()
v2 = len(v1)
v3 = int(1000000000.0 + 7)
v4 = [0] * v2
v5 = [0] * v2
v4[0] = 1
v5[0] = 2
for v6 in range(1, v2):
    v4[v6] += v4[v6 - 1] * 3
    v4[v6] %= v3
    if v1[v6] == '1':
        v4[v6] += v5[v6 - 1]
        v5[v6] += v5[v6 - 1] * 2
    else:
        v5[v6] += v5[v6 - 1]
    v4[v6] %= v3
    v5[v6] %= v3
print((v4[v2 - 1] + v5[v2 - 1]) % v3)
