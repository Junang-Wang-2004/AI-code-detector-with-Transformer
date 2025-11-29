from sys import exit
v1, v2, v3 = [int(n) for v4 in input().split()]
v5 = [[0 for v6 in range(v1 + 1)] for v7 in range(v2)]
v5[0][0] = 1
for v8 in range(1, v1 + 1):
    for v9 in range(1 << v2 - 1):
        v10 = bin(v9)[2:]
        v10 = v10[::-1]
        if '11' in v10:
            continue
        for v11 in range(v2):
            if v11 < len(v10) and v10[v11] == '1':
                v5[v11][v8] += v5[v11 + 1][v8 - 1]
                v5[v11 + 1][v8] += v5[v11][v8 - 1]
                v11 += 1
            else:
                v5[v11][v8] += v5[v11][v8 - 1]
print(v5[v3 - 1][v1])
exit()
