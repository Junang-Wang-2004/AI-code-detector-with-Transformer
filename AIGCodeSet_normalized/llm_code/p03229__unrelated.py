v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = 0
for v4 in range(v1 // 2):
    v3 += v2[v1 - 1 - v4] - v2[v4]
v5 = 0
for v4 in range(v1 // 2):
    v5 += v2[v1 - 2 - v4] - v2[v4]
v5 += v2[-1] - v2[0]
print(max(v3, v5))
