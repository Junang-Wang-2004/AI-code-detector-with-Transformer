v1 = input()

def f1(a1):
    v1 = len(a1)
    v2 = [[0 for v3 in range(4)] for v4 in range(v1 + 1)]
    v5 = 'ABC'
    v6 = 10 ** 9 + 7
    for v4 in range(v1, -1, -1):
        for v3 in range(3, -1, -1):
            if v4 == v1 and v3 == 3:
                v2[v4][v3] = 1
            elif v4 == v1 and v3 < 3:
                v2[v4][v3] = 0
            elif v4 < v1 and v3 == 3:
                if a1[v4] == '?':
                    v2[v4][v3] = 3 * v2[v4 + 1][v3] % v6
                else:
                    v2[v4][v3] = v2[v4 + 1][v3] % v6
            else:
                if a1[v4] == '?':
                    v7 = 3
                else:
                    v7 = 1
                if a1[v4] == '?' or a1[v4] == v5[v3]:
                    v8 = 1
                else:
                    v8 = 0
                v2[v4][v3] = v7 * v2[v4 + 1][v3] % v6 + v8 * v2[v4 + 1][v3 + 1] % v6
    return v2[0][0] % v6
print(f1(v1))
