v1, v2, v3 = map(int, input().split(' '))
v4 = {}
for v5 in range(v1):
    for v6, v7 in enumerate(map(int, input().split(' '))):
        v4[v7] = (v5, v6)
v8 = [0 for v5 in range(v1 * v2 + 1)]
for v5 in range(v1 * v2 + 1):
    if v5 + v3 <= v1 * v2:
        v8[v5 + v3] += v8[v5]
        if v5 != 0:
            v8[v5 + v3] += abs(v4[v5][0] - v4[v5 + v3][0]) + abs(v4[v5][1] - v4[v5 + v3][1])
v9 = int(input())
for v10 in range(v9):
    v11, v12 = map(int, input().split(' '))
    print(v8[v12] - v8[v11])
