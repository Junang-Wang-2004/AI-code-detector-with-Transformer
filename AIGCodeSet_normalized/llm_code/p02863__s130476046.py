v1, v2 = map(int, input().split())
v3 = [0] * 3001
v4 = [0] * 3001
v5 = [0] * 6001
for v6 in range(1, v1 + 1):
    v3[v6], v4[v6] = map(int, input().split())
for v6 in range(1, v1 + 1):
    for v7 in range(6000, v3[v6] - 1, -1):
        if v3[v6] <= v7 and v7 - v3[v6] < v2:
            v5[v7] = max(v5[v7], v5[v7 - v3[v6]] + v4[v6])
print(max(v5))
