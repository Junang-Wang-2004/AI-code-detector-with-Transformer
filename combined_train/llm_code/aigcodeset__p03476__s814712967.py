import math
import itertools
import bisect
import sys
input = sys.stdin.readline

def f1(a1):
    v1 = [1] * a1
    v1[0] = 0
    v2 = []
    for v3 in range(2, a1 + 1):
        if v1[v3 - 1]:
            v4 = 2 * v3
            while v4 <= a1:
                v1[v4 - 1] = 0
                v4 += v3
    for v3 in range(a1):
        if v1[v3] == 1:
            v2.append(v3)
    return v2

def f2(a1, a2=10 ** 9 + 7):
    return pow(a1, a2 - 2, a2)
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = f1(pow(10, 5) + 1)
for v3, v5 in v2:
    v6 = 0
    for v7 in range(v3, v5 + 1, 2):
        if v7 in v4 and (v7 + 1) // 2 in v4:
            v6 += 1
    print(v6)
