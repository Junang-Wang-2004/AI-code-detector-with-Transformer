v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4, v5 in enumerate(v2):
    v3.append([v5, v4])
v3.sort(reverse=True)
v6 = [[0] * (v1 + 1) for v7 in range(v1 + 1)]
for v4 in range(v1):
    for v8 in range(v4 + 1):
        v6[v4 + 1][v8 + 1] = max(v6[v4 + 1][v8 + 1], v6[v4][v8] + v3[v4][0] * abs(v3[v4][1] - v8))
        v6[v4 + 1][v8] = max(v6[v4 + 1][v8], v6[v4][v8] + v3[v4][0] * abs(v1 - 1 - (v4 - v8) - v3[v4][1]))
print(max(v6[v1]))
