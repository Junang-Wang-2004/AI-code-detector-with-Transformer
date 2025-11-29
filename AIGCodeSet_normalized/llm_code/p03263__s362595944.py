v1, v2 = [int(i) for v3 in input().split()]
v4 = [[int(v3) for v3 in input().split()] for v5 in range(v1)]
v4.append([0] * v2)
v6 = []
for v7 in range(v1):
    for v8 in range(v2 - 1):
        if v4[v7][v8] % 2 == 1:
            v4[v7][v8] -= 1
            v4[v7][v8 + 1] += 1
            v6.append((v7 + 1, v8 + 1, v7 + 1, v8 + 2))
    if v4[v7][v2 - 1] % 2 == 1:
        v4[v7 + 1][v2 - 1] += 1
        v6.append((v7 + 1, v2, v7 + 2, v2))
if v4[v1][v2 - 1] % 2 == 1:
    v6.pop()
print(len(v6))
for v7, v8, v9, v10 in v6:
    print(v7, v8, v9, v10)
