def f1():
    import sys
    v1 = sys.stdin.readline
    v2 = sys.stdout.write
    v3 = sys.stderr.write
    v4, v5, v6 = map(int, v1().split())
    v7 = [[]] * (v4 * v5)
    for v8 in range(v4):
        v9 = list(map(int, v1().split()))
        for v10 in range(v5):
            v7[v9[v10] - 1] = [v8, v10]
    v11 = int(v1())
    for v12 in range(v11):
        v13, v14 = map(int, v1().split())
        v15 = (v14 - v13) // v6
        v16 = 0
        v17 = v13 - 1
        for v18 in range(v15):
            v19 = v13 + v18 * v6 - 1
            v16 += abs(v7[v17][0] - v7[v19][0]) + abs(v7[v17][1] - v7[v19][1])
            v17 = v19
        print(v16)
    return
f1()
