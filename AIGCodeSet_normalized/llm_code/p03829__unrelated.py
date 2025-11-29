v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = [v4[i] - v4[i - 1] for v6 in range(1, v1)]
v7 = [0] * v1
v7[0] = 0
for v6 in range(1, v1):
    v7[v6] = min(v7[v6 - 1] + v2 * v5[v6 - 1], v7[v6 - 1] + v3)
print(v7[v1 - 1])
