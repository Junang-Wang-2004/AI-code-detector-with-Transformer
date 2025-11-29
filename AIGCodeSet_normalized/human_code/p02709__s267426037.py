from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def f1():
    v1 = int(input())
    v2 = [(int(v), i) for v3, v4 in enumerate(input().split())]
    v2.sort(reverse=True)
    v5 = [[0] * (v1 + 1) for v6 in range(v1 + 1)]
    v5[0][0] = v2[0][0] * (v1 - 1 - v2[0][1])
    v5[0][1] = v2[0][0] * v2[0][1]
    for v3, v4 in enumerate(v2[1:]):
        v5[v3 + 1][0] = v5[v3][0] + v4[0] * abs(v1 - 1 - (v3 + 1) - v4[1])
        v5[v3 + 1][v3 + 2] = v5[v3][v3 + 1] + v4[0] * abs(v4[1] - (v3 + 1))
        for v7 in range(1, v3 + 2):
            v5[v3 + 1][v7] = max(v5[v3][v7] + v4[0] * abs(v1 - 1 - (v3 + 1) + v7 - v4[1]), v5[v3][v7 - 1] + v4[0] * abs(v4[1] - (v7 - 1)))
    v8 = -float('inf')
    for v3 in v5[v1 - 1]:
        v8 = max(v8, v3)
    print(v8)
f1()
