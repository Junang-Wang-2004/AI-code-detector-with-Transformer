v1 = int(input())
v2 = v1 * (v1 - 1) // 2
for v3 in range(v1, v2 + 1):
    v4 = [[0] * v1 for v5 in range(v1)]
    v6 = 0
    for v7 in range(v1):
        v8 = v3 - sum(v4[v7])
        if v8 < 0:
            break
        for v9 in reversed(range(v7 + 1, v1)):
            if v8 - v7 - 1 > v9 + 1 or v8 == v9 + 1:
                v6 += 1
                v4[v7][v9] = v9 + 1
                v4[v9][v7] = v7 + 1
                v8 -= v9 + 1
            if v8 == 0:
                break
        else:
            continue
    else:
        print(v6)
        for v7 in range(v1):
            for v9 in range(v7 + 1, v1):
                if v4[v7][v9] > 0:
                    print(v7 + 1, v9 + 1)
        break
