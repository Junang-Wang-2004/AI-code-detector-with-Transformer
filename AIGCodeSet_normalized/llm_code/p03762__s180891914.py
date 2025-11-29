v1, v2 = [int(i) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = [int(v3) for v3 in input().split()]
v6 = 0
v7 = 10 ** 9 + 7
for v3 in range(v1):
    for v8 in range(v3 + 1, v1):
        for v9 in range(v2):
            for v10 in range(v9 + 1, v2):
                v11 = (v4[v8] - v4[v3]) * (v5[v10] - v5[v9])
                v6 = (v6 + v11) % v7
print(v6)
