v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    if v4 + 1 == v2[v4]:
        if v4 + 2 < v1:
            v5 = v2[v4 + 1]
            v2[v4 + 1] = v2[v4 + 2]
            v2[v4 + 2] = v5
            v3 += 1
        else:
            v5 = v2[v4]
            v2[v4] = v2[v4 - 1]
            v2[v4 - 1] = v5
            v3 += 1
print(v3)
