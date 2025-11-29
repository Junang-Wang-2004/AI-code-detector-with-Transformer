v1, v2 = map(int, input().split())
v3 = [[0] * int(100000.0) for v4 in range(v2)]
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split())
    v3[v8 - 1][v6 - 1:v7] = [1] * (v7 - v6 + 1)
print(max(map(sum, zip(*v3))))
