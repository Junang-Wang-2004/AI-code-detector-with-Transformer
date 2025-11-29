import sys
import math
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(1000000)
v1 = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
v2 = lambda: int(input())
v3 = lambda: map(int, input().split())
v4 = lambda: list(v3())
v5 = lambda: input()

def f1(a1, a2, a3):
    return [[int(a3)] * a2 for v1 in range(a1)]

def f2():
    v1, v2, v3 = v3()
    v4 = f1(v1, v2, 0)
    for v5 in range(v3):
        v6, v7, v8 = v3()
        v4[v6 - 1][v7 - 1] = v8
    v9 = [[0 for v10 in range(v2 + 2)] for v10 in range(v1 + 2)]
    v11 = [[0 for v10 in range(v2 + 2)] for v10 in range(v1 + 2)]
    v12 = [[0 for v10 in range(v2 + 2)] for v10 in range(v1 + 2)]
    v13 = [[0 for v10 in range(v2 + 2)] for v10 in range(v1 + 2)]
    for v6 in range(v1 + 1):
        for v7 in range(v2 + 1):
            v14 = v9[v6][v7]
            v15 = v11[v6][v7]
            v16 = v12[v6][v7]
            v17 = v13[v6][v7]
            try:
                v18 = v4[v6][v7]
            except:
                v18 = 0
            v9[v6 + 1][v7] = max(v17, v9[v6 + 1][v7])
            v9[v6 + 1][v7] = max(v14 + v18, v15 + v18, v16 + v18, v9[v6 + 1][v7])
            v9[v6 + 1][v7] = max(v14, v15, v16, v17, v9[v6 + 1][v7])
            v11[v6][v7 + 1] = max(v14 + v18, v11[v6][v7 + 1])
            v12[v6][v7 + 1] = max(v15 + v18, v12[v6][v7 + 1])
            v13[v6][v7 + 1] = max(v16 + v18, v13[v6][v7 + 1])
            v11[v6][v7 + 1] = max(v15, v11[v6][v7 + 1])
            v12[v6][v7 + 1] = max(v16, v12[v6][v7 + 1])
            v9[v6][v7 + 1] = max(v14, v9[v6][v7 + 1])
    print(max(v9[v1][v2], v11[v1][v2], v12[v1][v2], v13[v1][v2]))
if __name__ == '__main__':
    f2()
