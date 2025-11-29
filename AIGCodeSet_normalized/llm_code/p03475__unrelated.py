v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1 - 1)]
v4 = [0] * v1
for v5 in range(v1 - 2, -1, -1):
    v6, v7, v8 = v2[v5]
    v9 = float('inf')
    for v10 in range(v7, 10 ** 5 + 1, v8):
        if v10 + v6 >= v4[v5 + 1]:
            v9 = v10 + v6
            break
    v4[v5] = v9
for v5 in range(v1):
    print(v4[v5])
