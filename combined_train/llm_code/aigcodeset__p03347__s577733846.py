import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def f1():
    return list(map(int, input().split(' ')))

def f2():
    return int(input())
v1 = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
v1 = list(map(np.array, v1))
v2 = 10 ** 9 + 7

def f3(a1):
    v1 = 1
    for v2 in range(1, a1 + 1):
        v1 *= v2
    return v1

def f4(a1, a2):
    for v1 in v1:
        v2 = v1 + a1
        if np.all(0 <= v2) and np.all(v2 < (H, W)):
            if field[v2[0]][v2[1]] == 'E':
                a2 += 1
                field[v2[0]][v2[1]] = 'V'
                a2 = f4(v2, a2)
                continue
            if field[v2[0]][v2[1]] == '#':
                field[v2[0]][v2[1]] = 'V'
                a2 = f4(v2, a2)
    return a2
v3 = int(input())
v4 = []
for v5 in range(v3):
    v4.append(f2())
if v4[0] > 0:
    print(-1)
    sys.exit()
for v5 in range(1, v3):
    if v4[v5] - v4[v5 - 1] > 1:
        print(-1)
        sys.exit()
v6 = 0
v7 = [0] * v3
for v5 in reversed(range(v3)):
    if v4[v5] != v7[v5]:
        for v8 in range(v5 - v4[v5], v5):
            v7[v8 + 1] = v7[v8] + 1
            v6 += 1
print(v6)
