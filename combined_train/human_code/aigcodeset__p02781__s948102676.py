def f1():
    v1 = input()
    v2 = int(input())
    v3 = len(v1)
    v4 = [[[0] * 2 for v5 in range(4)] for v5 in range(v3 + 1)]
    v4[0][0][0] = 1
    for v6 in range(v3):
        for v7 in range(4):
            for v8 in range(2):
                v9 = int(v1[v6])
                for v10 in range(10):
                    v11 = v6 + 1
                    v12 = v7
                    v13 = v8
                    if v10 != 0:
                        v12 += 1
                    if v12 > v2:
                        continue
                    if v8 == 0:
                        if v10 > v9:
                            continue
                        if v10 < v9:
                            v13 = 1
                    v4[v11][v12][v13] += v4[v6][v7][v8]
    v14 = v4[v3][v2][0] + v4[v3][v2][1]
    print(v14)
if __name__ == '__main__':
    f1()
