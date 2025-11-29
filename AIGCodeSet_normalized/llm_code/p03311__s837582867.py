v1 = int(input())
v2 = list(map(int, input().split()))
for v3 in range(v1):
    v2[v3] -= v3 + 1
v4 = sum(v2) / v1
v5 = int(v4)
v6 = v5 + 1
v2.sort()
v7 = 0
v8 = 0
for v3 in v2:
    v7 += abs(v3 - v5)
    v8 += abs(v3 - v6)
print(min([v7, v8]))
