v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = [[0 for v7 in range(v2 + 1)] for v8 in range(v1 + 1)]
for v7 in range(v1):
    for v8 in range(v2):
        if v4[v7] == v5[v8]:
            v6[v7 + 1][v8 + 1] = (2 * v6[v7][v8] + 1) % v3
        else:
            v6[v7 + 1][v8 + 1] = v6[v7][v8 + 1] + v6[v7 + 1][v8] - v6[v7][v8]
            v6[v7 + 1][v8 + 1] %= v3
print(v6[v1][v2] + 1)
