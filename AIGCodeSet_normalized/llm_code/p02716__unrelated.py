v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [[0, 0] for v4 in range(v1)]
v3[0][1] = v2[0]
for v5 in range(1, v1):
    v3[v5][1] = v3[v5 - 2][0] + v2[v5]
    v3[v5][0] = max(v3[v5 - 1][0], v3[v5 - 1][1])
print(max(v3[v1 - 1][0], v3[v1 - 1][1]))
