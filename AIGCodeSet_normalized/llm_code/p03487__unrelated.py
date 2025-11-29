v1 = int(input())
v2 = list(map(int, input().split()))
v3 = {}
for v4 in v2:
    if v4 in v3:
        v3[v4] += 1
    else:
        v3[v4] = 1
v5 = 0
for v4 in v3:
    v5 += abs(v3[v4] - v4)
print(v5 // 2)
