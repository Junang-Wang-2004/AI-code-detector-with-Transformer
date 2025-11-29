def f1():
    v1 = 40001
    v2, v3, v4 = list(map(int, input().split(' ')))
    v5, v6, v7 = (list(), list(), list())
    for v8 in range(v2):
        v9, v10, v11 = list(map(int, input().split(' ')))
        v5.append(v9)
        v6.append(v10)
        v7.append(v11)
    v12 = [[v1 for v8 in range(8001)] for v8 in range(v2 + 1)]
    v12[0][0] = 0
    for v13 in range(1, v2 + 1):
        v9, v10, v11 = (v5[v13 - 1], v6[v13 - 1], v7[v13 - 1])
        for v14 in range(8001):
            if v12[v13 - 1][v14] != v1:
                v12[v13][v14] = min(v12[v13][v14], v12[v13 - 1][v14])
                v12[v13][v14 + (v4 * v9 - v3 * v10)] = min(v12[v13][v14 + (v4 * v9 - v3 * v10)], v12[v13 - 1][v14] + v11)
    v15 = v12[v2][0]
    if v15 >= v1:
        v15 = -1
    print(v15)
if __name__ == '__main__':
    f1()
