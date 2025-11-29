from bisect import bisect_left

def f1(a1, a2, a3):
    v1 = len(a1)
    v2 = []
    for v3 in range(2 ** v1):
        v4 = bin(v3)[2:]
        if len(v4) < v1:
            v5 = '0' * (v1 - len(v4))
            v4 = v5 + v4
        v6, v7, v8 = (0, 0, 0)
        for v9 in range(len(v4)):
            if v4[v9] == '1':
                v6 += a1[v9][0]
                v7 += a1[v9][1]
                v8 += a1[v9][2]
        v10 = a3 * v6 - a2 * v7
        v2.append((v10, v8))
    v2.sort(key=lambda x: x[0])
    return v2

def f2():
    v1, v2, v3 = map(int, input().split())
    v4 = [list(map(int, input().split())) for v5 in range(v1)]
    v6 = 4001
    v7, v8 = (v4[:len(v4) // 2], v4[len(v4) // 2:])
    v9, v10 = (f1(v7, v2, v3), f1(v8, v2, v3))
    v11 = [v10[i][0] for v12 in range(len(v10))]
    v13 = set(v11)
    v14 = v6
    for v12 in range(len(v9)):
        v15, v16 = (v9[v12][0], v9[v12][1])
        if -v15 in v13:
            v17 = bisect_left(v11, -v15)
            v18 = v10[v17][1]
            if v16 + v18 < v14:
                v14 = v16 + v18
    if len(v9) == 0:
        if v10[0][0] == 0:
            v14 = min(v14, v10[0][1])
    if v14 != v6:
        print(v14)
    else:
        print(-1)
if __name__ == '__main__':
    f2()
