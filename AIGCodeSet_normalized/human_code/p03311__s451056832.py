v1 = int(input())
v2 = list(map(int, input().split()))
for v3 in range(v1):
    v2[v3] -= v3 + 1
v2.sort()
v4 = v2[v1 // 2]
v5 = v2[v1 // 2 - 1]
v6 = sum([abs(ele - v4) for v7 in v2])
v8 = sum([abs(v7 - v5) for v7 in v2])
print(min(v6, v8))
