v1 = input()
v2 = int(input())
v3 = len(v1)
if v3 == 1:
    print([0, int(v1)][v2 == 1])
    exit()
v4 = [[[0] * 2 for v5 in range(v2 + 1)] for v5 in range(v3)]
v4[0][0][1] = 1
v4[0][1][1] = int(v1[0]) - 1
v4[0][1][0] = 1
for v6 in range(1, v3):
    for v7 in range(v2 + 1):
        if v7:
            v4[v6][v7][1] += 9 * v4[v6 - 1][v7 - 1][1]
            if v1[v6] != '0':
                v4[v6][v7][0] += v4[v6 - 1][v7 - 1][0]
                v4[v6][v7][1] += (int(v1[v6]) - 1) * v4[v6 - 1][v7 - 1][0]
        if v1[v6] == '0':
            v4[v6][v7][0] += v4[v6 - 1][v7][0]
        v4[v6][v7][1] += v4[v6 - 1][v7][1]
        if v1[v6] != '0':
            v4[v6][v7][1] += v4[v6 - 1][v7][0]
print(sum(v4[-1][-1]))
