import numpy as np
if __name__ == '__main__':
    v1 = lambda: [int(x) for v2 in input().split()]
    v3, v4, v5 = v1()
    v6 = np.array([v1() for v7 in range(v3)])
    v8 = 100 * v3 + 1
    v9 = np.ones((v3 + 1, v3 * 10 + 1, v3 * 10 + 1)) * v8
    v9[0, 0, 0] = 0
    for v7 in range(v3):
        for v10 in range(v3 * 10 + 1):
            for v11 in range(v3 * 10 + 1):
                if v9[v7, v10, v11] == v8:
                    continue
                v9[v7 + 1, v10, v11] = min(v9[v7 + 1, v10, v11], v9[v7, v10, v11])
                v9[v7 + 1, v10 + v6[v7, 0], v11 + v6[v7, 1]] = min(v9[v7 + 1, v10 + v6[v7, 0], v11 + v6[v7, 1]], v9[v7, v10, v11] + v6[v7, 2])
    v12 = v8
    for v10 in range(1, v3 * 10 + 1):
        for v11 in range(1, v3 * 10 + 1):
            if v4 * v11 == v5 * v10 and v9[v3, v10, v11] < v12:
                v12 = v9[v3, v10, v11]
    if v12 == v8:
        v12 = -1
    print(int(v12))
