v1 = int(input())
v2, v3 = [list(map(int, input().split())) for v4 in range(2)]
v5 = 0
for v4 in range(v1):
    v5 += min(v2[v4], v3[v4])
    v3[v4] = max(0, v3[v4] - v2[v4])
    v5 += min(v2[v4 + 1], v3[v4])
    v2[v4 + 1] = max(0, v2[v4 + 1] - v3[v4])
print(v5)
