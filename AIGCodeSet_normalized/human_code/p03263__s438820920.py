v1, v2 = [int(s) for v3 in input().split()]
v4 = [[int(v3) for v3 in input().split()] for v5 in range(v1)]
v6 = []
for v5 in range(v1):
    for v7 in range(v2 - 1):
        if v4[v5][v7] % 2 == 1:
            v6.append([v5 + 1, v7 + 1, v5 + 1, v7 + 2])
            v4[v5][v7 + 1] += 1
for v5 in range(v1 - 1):
    if v4[v5][v2 - 1] % 2 == 1:
        v6.append([v5 + 1, v2, v5 + 2, v2])
        v4[v5 + 1][v2 - 1] += 1
print(len(v6))
for v8 in v6:
    print(*v8)
