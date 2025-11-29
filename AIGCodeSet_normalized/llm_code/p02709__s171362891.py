v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4, v5 in enumerate(v2):
    v3.append([v5, v4])
v3.sort(reverse=True)
v6 = [[0 for v4 in range(v1 + 1)] for v7 in range(v1 + 1)]
for v4 in range(1, v1 + 1):
    v8, v9 = v3.pop()
    for v10 in range(v4 + 1):
        v11 = v4 - v10
        v6[v10][v11] = max((v6[v10 - 1][v11] + v8 * abs(v9 - v10 + 1)) * (v10 > 0), v6[v10][v11 - 1] + v8 * abs(v9 - (v1 - v11)) * (v11 > 0))
v12 = 0
for v4 in range(v1 + 1):
    v12 = max(v12, v6[v4][v1 - v4])
print(v12)
