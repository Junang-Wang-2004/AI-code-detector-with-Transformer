v1 = input()
v2 = [[0] * (len(v1) + 1) for v3 in range(4)]
v2[3][-1] += 1
v4 = 'ABC'
for v5 in range(len(v1) - 1, -1, -1):
    for v6 in range(3, -1, -1):
        if v6 == 3:
            if v1[v5] == '?':
                v2[3][v5] = v2[3][v5 + 1] * 3
            else:
                v2[3][v5] = v2[3][v5 + 1]
        elif v1[v5] == '?':
            v2[v6][v5] = 3 * v2[v6][v5 + 1] + v2[v6 + 1][v5 + 1]
        else:
            v2[v6][v5] = v2[v6][v5 + 1]
            if v4[v6] == v1[v5]:
                v2[v6][v5] += v2[v6 + 1][v5]
print(v2[0][0])
