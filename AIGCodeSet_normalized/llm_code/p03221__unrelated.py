v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v3.sort(key=lambda x: x[1])
v5 = [0] * (v1 + 1)
for v6 in range(v2):
    v7 = v3[v6][0]
    v5[v7] += 1
    v8 = str(v7).zfill(6) + str(v5[v7]).zfill(6)
    print(v8)
