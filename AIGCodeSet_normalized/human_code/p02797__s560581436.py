v1, v2, v3 = map(int, input().split())
v4 = [0 for v5 in range(v1)]
if v3 > 2:
    for v6 in range(v1):
        if v6 < v1 - v2:
            v4[v6] = v3 - 1
        else:
            v4[v6] = v3
else:
    for v6 in range(v1):
        if v6 < v1 - v2:
            v4[v6] = v3 + 1
        else:
            v4[v6] = v3
print(*v4)
