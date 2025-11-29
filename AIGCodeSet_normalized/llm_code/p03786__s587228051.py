v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = v1
v4 = v2[0]
v5 = 1
for v6 in range(1, v1):
    if v2[v6] <= v4 * 2:
        v4 += v2[v6]
        v5 += 1
    else:
        v4 = v2[v6]
        v3 -= v5
        v5 = 1
print(v3)
