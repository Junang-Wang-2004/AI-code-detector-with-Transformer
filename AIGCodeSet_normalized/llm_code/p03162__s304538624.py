v1 = int(input())
v2 = [[0, 0, 0] for v3 in range(v1 + 1)]
for v4 in range(1, v1 + 1):
    v5 = list(map(int, input().split()))
    v2[v4][0] = max(v2[v4 - 1][1], v2[v4 - 1][2]) + v5[0]
    v2[v4][1] = max(v2[v4 - 1][0], v2[v4 - 1][2]) + v5[1]
    v2[v4][2] = max(v2[v4 - 1][0], v2[v4 - 1][1]) + v5[2]
print(max(v2[v1]))
