v1 = int(input())
v2 = list(map(int, input().split()))
v2 = [v2[i] - (i + 1) for v3 in range(v1)]
v2.sort()
v4 = v2[v1 // 2]
v5 = v2[(v1 - 1) // 2]
v6 = 0
for v3 in range(v1):
    v6 += abs(v2[v3] - v4)
v7 = 0
for v8 in range(v1):
    v7 += abs(v2[v8] - v5)
print(min(v6, v7))
