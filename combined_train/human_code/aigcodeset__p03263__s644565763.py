v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v1)]
for v4 in range(v1):
    v3[v4] = list(map(int, input().split()))
v5 = []
for v4 in range(v1):
    for v6 in range(v2):
        if v4 == v1 - 1 and v6 == v2 - 1:
            continue
        if v6 == v2 - 1 and v3[v4][v6] % 2 == 1 and (v4 < v1 - 1):
            v3[v4][v6] -= 1
            v3[v4 + 1][v6] += 1
            v5.append([v4 + 1, v6 + 1, v4 + 2, v6 + 1])
        elif v3[v4][v6] % 2 == 1:
            v3[v4][v6] -= 1
            v3[v4][v6 + 1] += 1
            v5.append([v4 + 1, v6 + 1, v4 + 1, v6 + 2])
print(len(v5))
for v4 in range(len(v5)):
    print('%d %d %d %d' % (v5[v4][0], v5[v4][1], v5[v4][2], v5[v4][3]))
