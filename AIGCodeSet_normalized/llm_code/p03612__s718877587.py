v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    v5 = v2[v4]
    v6 = v4 + 1
    if v5 == v6:
        if v6 == 1:
            v3 += 1
            v2[v4], v2[v4 + 1] = (v2[v4 + 1], v2[v4])
        else:
            v3 += 1
            v2[v4 - 1], v2[v4] = (v2[v4], v2[v4 - 1])
print(v3)
