v1, v2 = [int(x) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = 0
for v6 in range(v2 + 1):
    for v7 in range(v6 + 1):
        for v8 in range(v6 - v7 + 1):
            v9 = sorted(v4[0:v7] + v4[v1 - v8:])
            if len(v9) <= v2 - v6:
                for v10 in range(len(v9)):
                    if v9[v10] > 0:
                        break
                v5 = max(v5, sum(v9[v10:]))
            elif v9[v2 - v6 - 1] < 0:
                v5 = max(v5, sum(v9[v2 - v6:]))
            else:
                for v10 in range(v2 - v6):
                    if v9[v10] > 0:
                        break
                v5 = max(v5, sum(v9[v10:]))
print(v5)
