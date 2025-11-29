v1 = int(input())
v2 = input()
v3 = [[False, [[False, [False for v4 in range(10)]] for v5 in range(10)]] for v6 in range(10)]
v7 = 0
for v8 in v2:
    v8 = int(v8)
    for v6 in range(10):
        if v3[v6][0]:
            for v5 in range(10):
                if v3[v6][1][v5][0]:
                    if not v3[v6][1][v5][1][v8]:
                        v7 += 1
                        v3[v6][1][v5][1][v8] = True
            v3[v6][1][v8][0] = True
    v3[v8][0] = True
print(v7)
