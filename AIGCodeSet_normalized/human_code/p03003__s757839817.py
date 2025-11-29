def f1():
    v1 = 10 ** 9 + 7
    v2, v3 = list(map(int, input().split(' ')))
    v4 = list(map(int, input().split(' ')))
    v5 = list(map(int, input().split(' ')))
    v6 = [[0 for v7 in range(v3 + 1)] for v7 in range(v2 + 1)]
    v8 = [[0 for v7 in range(v3 + 1)] for v7 in range(v2 + 1)]
    for v9, v10 in enumerate(v4):
        for v11, v12 in enumerate(v5):
            v13 = v8[v9][v11]
            v14 = v13 + 1 if v10 == v12 else 0
            v6[v9 + 1][v11 + 1] = v14 % v1
            v8[v9 + 1][v11 + 1] = (v8[v9][v11 + 1] + v8[v9 + 1][v11] - v13 + v14) % v1
    print((v8[v2][v3] + 1) % v1)
if __name__ == '__main__':
    f1()
