from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def f1():
    v1, v2, v3 = (int(i) for v4 in input().split())
    v5 = []
    for v4 in range(v1):
        v6 = list((int(v4) for v4 in input().split()))
        v5.append(v6)
    v7 = [False] * (v1 * v2)
    v8 = [0] * (v1 * v2 + 1)
    for v4 in range(v1):
        for v9 in range(v2):
            v10 = v5[v4][v9] - 1
            v7[v10] = (v4, v9)
    v11 = int(input())
    for v4 in range(v3, v1 * v2):
        v12, v13 = v7[v4 - v3]
        v14, v15 = v7[v4]
        v8[v4] = v8[v4 - v3] + abs(v14 - v12) + abs(v15 - v13)
    for v4 in range(v11):
        v16, v17 = (int(m) for v18 in input().split())
        print(v8[v17 - 1] - v8[v16 - 1])
f1()
