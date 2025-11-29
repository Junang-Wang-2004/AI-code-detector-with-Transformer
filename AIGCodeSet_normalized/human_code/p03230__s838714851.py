v1 = int(input())
v2 = 2
while 2 * v1 > v2 * (v2 - 1):
    v2 += 1
if 2 * v1 != v2 * (v2 - 1):
    print('No')
else:
    print('Yes')
    print(v2)
    v3 = 0
    v4 = [[0] * (v2 - 1) for v5 in range(v2)]
    for v5 in range(v2):
        for v6 in range(v5):
            v4[v5][v6] = v4[v6][v5 - 1]
        for v7 in range(v2 - v5 - 1):
            v3 += 1
            v4[v5][v5 + v7] = v3
    for v6 in range(v2):
        print('{} '.format(v2 - 1), end='')
        for v5 in range(v2 - 2):
            print('{} '.format(v4[v6][v5]), end='')
        print(v4[v6][v2 - 2])
