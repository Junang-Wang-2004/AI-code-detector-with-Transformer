def f1(a1):
    v1 = len(a1)
    v2 = [[0] * (v1 + 1) for v3 in range(v1 + 1)]
    for v4 in range(v1 - 1, -1, -1):
        for v5 in range(v4, v1 + 1):
            if v5 - v4 < 2:
                v2[v4][v5] = (1, v5 - v4)
            else:
                v2[v4][v5] = (float('inf'), 0)
                for v6 in range(v4 + 1, v5):
                    v7 = v2[v4][v6]
                    v8 = v2[v6][v5]
                    if v7[0] == v8[0]:
                        if v7[1] + v8[1] < v2[v4][v5][0]:
                            v2[v4][v5] = (v7[0], v7[1] + v8[1])
                        elif v7[1] + v8[1] == v2[v4][v5][0]:
                            v2[v4][v5] = (min(v2[v4][v5][1], v7[1] + v8[1] + (1 if a1[v6 - 1] == '(' else -1)), v2[v4][v5][1])
                    elif v7[0] < v8[0]:
                        v2[v4][v5] = (v7[0], v7[1] + v8[1])
    v9 = []
    v4, v5 = (0, v1)
    while v4 < v5:
        if v2[v4][v5][0] == 1:
            v9.append(a1[v4:v5])
            v4 = v5
        else:
            for v6 in range(v4 + 1, v5):
                if v2[v4][v6][0] == v2[v6][v5][0] and v2[v4][v6][1] + v2[v6][v5][1] == v2[v4][v5][0]:
                    v9.append('(')
                    v9.extend(f1(a1[v4 + 1:v6]))
                    v9.append(')')
                    v9.extend(f1(a1[v6:v5]))
                    break
    return v9
v1 = int(input())
v2 = input()
print(''.join(f1(v2)))
