v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = 10000000000
v6 = 0
for v4 in range(2 ** v1):
    v7 = 0
    v6 = 0
    for v8 in range(v1):
        if 1 & v4 >> v8:
            v7 += v3[v1 - 1 - v8][0]
            v6 += (v1 - v8) * 100 * v3[v1 - 1 - v8][0] + v3[v1 - 1 - v8][1]
    if v6 >= v2:
        v5 = min(v5, v7)
    else:
        for v9 in reversed(range(v1)):
            if bin(v4)[2:].zfill(v1)[v9] == '1':
                continue
            for v10 in range(v3[v9][0]):
                v6 += (v9 + 1) * 100
                v7 += 1
                if v6 >= v2:
                    v5 = min(v5, v7)
        v5 = min(v5, v7)
print(v5)
