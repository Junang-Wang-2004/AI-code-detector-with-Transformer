import sys
input = sys.stdin.readline
import numpy as np

def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return list(map(int, input().split()))
v1 = f1()
v2 = [list(f2()) for v3 in range(v1 - 1)]

def f4(a1):
    v1 = 0
    for v2 in range(a1, v1 - 1):
        v3, v4, v5 = v2[v2]
        if v1 < v4:
            v1 = v4
        v1 += v5 - (v1 - v4) % v5 + v3
    print(v1)
for v3 in range(v1 - 1):
    f4(v3)
print(0)
