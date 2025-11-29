v1 = 10 ** 5 + 1
v2 = [True] * (v1 + 1)
v2[0] = False
v2[1] = False
for v3 in range(2, v1 + 1):
    if v2[v3]:
        for v4 in range(v3 * 2, v1 + 1, v3):
            v2[v4] = False
v5 = [0] * (v1 + 1)
for v3 in range(0, v1 + 1):
    if v3 % 2 == 0:
        continue
    if v2[v3] and v2[(v3 + 1) // 2]:
        v5[v3] = 1
v6 = [0] * (v1 + 1)
for v3 in range(v1):
    v6[v3 + 1] = v6[v3] + v5[v3]
v7 = int(input())
v8 = [list(map(int, input().split())) for v9 in range(v7)]
for v3 in range(v7):
    print(v6[v8[v3][1] + 1] - v6[v8[v3][0]])
