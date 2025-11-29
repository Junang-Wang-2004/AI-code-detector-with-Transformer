v1 = list(input())
v2 = [0]
for v3 in range(len(v1) - 1):
    if v1[v3] == 'R' and v1[v3 + 1] == 'L' or (v1[v3] == 'L' and v1[v3 + 1] == 'R'):
        v2 += [v3, v3 + 1]
v2.append(len(v1) - 1)
v4 = []
for v3 in range(len(v2) // 4):
    v5 = v2[4 * v3 + 1] - v2[4 * v3] + 1
    v6 = v2[4 * v3 + 3] - v2[4 * v3 + 2] + 1
    if (v5 + v6) % 2 == 0:
        v4 += [0] * (v5 - 1) + [(v5 + v6) // 2] * 2 + [0] * (v6 - 1)
    elif v5 % 2 == 1:
        v4 += [0] * (v5 - 1) + [(v5 + v6 + 1) // 2, (v5 + v6 - 1) // 2] + [0] * (v6 - 1)
    else:
        v4 += [0] * (v5 - 1) + [(v5 + v6 - 1) // 2, (v5 + v6 + 1) // 2] + [0] * (v6 - 1)
for v3 in range(len(v4)):
    if v3 != len(v4) - 1:
        print(v4[v3], end=' ')
    else:
        print(v4[v3])
