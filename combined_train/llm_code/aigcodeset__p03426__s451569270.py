import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
v1 = 10 ** 9 + 7
from collections import defaultdict
v2, v3, v4 = map(int, input().split())
v5 = [list(map(int, input().split())) for v6 in range(v2)]
v7 = defaultdict(list)
for v8 in range(v2):
    for v9 in range(v3):
        v7[v5[v8][v9]] = [v8, v9]

def f1(a1, a2):
    return abs(v7[a1][0] - v7[a2][0]) + abs(v7[a1][1] - v7[a2][1])
v10 = [0] * (v2 * v3 + 1)
for v11 in range(1, v4 + 1):
    v12 = v11
    while v12 + v4 <= v2 * v3:
        v10[v12 + v4] = v10[v12] + f1(v12, v12 + v4)
        v12 += v4
v13 = int(input())
for v6 in range(v13):
    v14, v15 = map(int, input().split())
    v16 = v10[v15] - v10[v14]
    print(v16)
