import math
import collections
import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def f1():
    v1 = int(input())
    v2 = v1 * (v1 - 1) // 2
    v3 = [list(map(int, input().split())) for v4 in range(v1)]
    for v4 in range(v1):
        for v5 in range(v1 - 1):
            v3[v4][v5] -= 1
    v6 = 0
    v7 = [[0 for v4 in range(v1)] for v5 in range(v1)]
    for v4 in range(v1):
        for v5 in range(v1):
            if v4 < v5:
                v7[v4][v5] = v6
                v6 += 1

    def toId(a1, a2):
        if a1 > a2:
            a1, a2 = (a2, a1)
        return v7[a1][a2]
    v8 = [[] for v4 in range(v2)]
    for v4 in range(v1):
        for v5 in range(v1 - 1):
            v3[v4][v5] = toId(v4, v3[v4][v5])
        for v5 in range(v1 - 2):
            v8[v3[v4][v5 + 1]].append(v3[v4][v5])
    v9 = [False for v4 in range(v2)]
    v10 = [False for v4 in range(v2)]
    v11 = [-1 for v4 in range(v2)]

    def dfs(a1):
        if v11[a1] != -1:
            if not v10[a1]:
                return -1
            return v11[a1]
        v9[a1] = True
        v11[a1] = 1
        for v1 in v8[a1]:
            v2 = dfs(v1)
            if v2 == -1:
                return -1
            v11[a1] = max(v11[a1], v2 + 1)
        v10[a1] = True
        return v11[a1]
    v12 = 0
    for v4 in range(v6):
        v13 = dfs(v4)
        if v13 == -1:
            print(-1)
            exit()
        v12 = max(v12, v13)
    print(v12)
if __name__ == '__main__':
    f1()
