v1, v2 = map(int, input().split())
v3 = [[0] * 100001 for v4 in range(v2)]
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split())
    v3[v8 - 1][v6] += 1
    v3[v8 - 1][v7] -= 1
for v8 in range(v2):
    for v5 in range(1, 100001):
        v3[v8][v5] += v3[v8][v5 - 1]
print(max(map(sum, zip(*v3))))
