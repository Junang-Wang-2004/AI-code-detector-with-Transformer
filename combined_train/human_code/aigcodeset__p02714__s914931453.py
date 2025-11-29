def f1():
    v1 = int(input())
    v2 = list(input())
    v3 = [[0] * 3 for v4 in range(v1)]
    v3[0][0], v3[0][1], v3[0][2] = (v2.count('R'), v2.count('G'), v2.count('B'))
    v5 = 0

    def num(a1):
        if a1 == 'R':
            return 0
        elif a1 == 'G':
            return 1
        else:
            return 2
    for v6 in range(v1 - 1):
        v3[v6 + 1][0], v3[v6 + 1][1], v3[v6 + 1][2] = (v3[v6][0], v3[v6][1], v3[v6][2])
        v3[v6 + 1][num(v2[v6])] -= 1
    for v6 in range(v1 - 2):
        for v7 in range(v6 + 1, v1 - 1):
            if v2[v6] == v2[v7]:
                continue
            else:
                v5 += v3[v7 + 1][3 - num(v2[v6]) - num(v2[v7])]
                if 2 * v7 - v6 <= v1 - 1:
                    if v2[v6] != v2[2 * v7 - v6] and v2[v7] != v2[2 * v7 - v6]:
                        v5 -= 1
    print(v5)
if __name__ == '__main__':
    f1()
