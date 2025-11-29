v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, list(input()))) for v5 in range(v1)]
v6 = []
for v7 in range(2 ** (v1 - 1)):
    v8, v9 = (0, v7)
    while v9 > 0:
        v8 += v9 % 2
        v9 >>= 1
    v8 = format(v7, '0' + str(v1) + 'b').count('1')
    v10 = 0
    v11 = [0 for v5 in range(v8 + 1)]
    for v12 in range(v2):
        v9 = v7
        v13 = 0
        v14 = [0 for v5 in range(v8 + 1)]
        for v15 in range(v1):
            v14[v13] += v4[v15][v12]
            v13 += v9 % 2
            v9 = v9 >> 1
        if all((v14[v15] + v11[v15] <= v3 for v15 in range(v8 + 1))):
            v11 = [v11[I] + v14[I] for v16 in range(v8 + 1)]
        else:
            v10 += 1
            v11 = v14
    v6.append(v8 + v10)
print(min(v6))
