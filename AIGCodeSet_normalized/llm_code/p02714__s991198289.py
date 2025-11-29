v1 = int(input())
v2 = input()
v3 = v2.count('R')
v4 = v2.count('G')
v5 = v2.count('B')
v6 = v3 * v4 * v5
if v6 == 0:
    print(0)
else:
    v7 = []
    v8 = []
    v9 = []
    for v10 in range(v1):
        if v2[v10] == 'R':
            v7.append(v10)
        elif v2[v10] == 'G':
            v8.append(v10)
        else:
            v9.append(v10)
    v11 = 0
    for v10 in v7:
        for v12 in v8:
            if 0 <= 2 * v12 - v10 < v1 and v2[2 * v12 - v10] == 'B':
                v11 += 1
            if 0 <= 2 * v10 - v12 < v1 and v2[2 * v10 - v12] == 'B':
                v11 += 1
            if (v10 + v12) % 2 == 0 and v2[(v10 + v12) // 2] == 'B':
                v11 += 1
    print(v6 - v11)
