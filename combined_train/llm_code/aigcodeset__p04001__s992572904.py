import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def f1(a1):
    v1 = 0
    for v2 in range(len(a1) - 1, 0, -1):
        v1 += int(a1[v2]) * 10 ** (len(a1) - 1 - v2)
    return v1
v1 = input()
v2 = len(v1)
v3 = 0
for v4 in range(2 ** v2):
    v5 = 0
    for v6 in range(v2):
        if v4 & 1 << v6:
            v3 += f1(v1[v5:v6 - v5])
            v5 = v6 + 1
    v3 += f1(v1[v5:])
print(v3)
