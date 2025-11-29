import sys
input = sys.stdin.readline

def f1():
    v1 = float('inf')

    def WarshallFloyd(a1, a2):
        v1 = len(a1)
        v2 = [[a2] * v1 for v3 in range(v1)]
        for v4, v5 in enumerate(a1):
            for v6, v7 in v5:
                v2[v4][v6] = v7
            v2[v4][v4] = 0
        for v8 in range(v1):
            v9 = v2[v8]
            for v10 in range(v1):
                v11 = v2[v10]
                v12 = v11[v8]
                for v13 in range(v1):
                    v14 = v12 + v9[v13]
                    if v14 < v11[v13]:
                        v2[v10][v13] = v14
        return v2
    v2, v3, v4 = map(int, input().split())
    v5 = [[] for v6 in range(v2)]
    for v6 in range(v3):
        v7, v8, v9 = map(int, input().split())
        v7, v8 = (v7 - 1, v8 - 1)
        v5[v7].append((v8, v9))
        v5[v8].append((v7, v9))
    v10 = int(input())
    v11 = [tuple(map(int, input().split())) for v6 in range(v10)]
    v12 = WarshallFloyd(v5, v1)
    v13 = [[] for v6 in range(v2)]
    for v7 in range(v2):
        for v8 in range(v7 + 1, v2):
            if v12[v7][v8] <= v4:
                v13[v7].append((v8, 1))
                v13[v8].append((v7, 1))
    v14 = WarshallFloyd(v13, v1)
    v15 = []
    for v16, v17 in v11:
        v16, v17 = (v16 - 1, v17 - 1)
        v18 = v14[v16][v17]
        if v18 == v1:
            v15.append(-1)
        else:
            v15.append(v18 - 1)
    print('\n'.join(map(str, v15)))
f1()
