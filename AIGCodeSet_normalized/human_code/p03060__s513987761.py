import math
import collections
import sys
input = sys.stdin.readline

def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return list(map(int, input().split()))

def f4():
    return [int(input()) for v1 in range(n)]

def f5():
    return [[f3()] for v1 in range(n)]
v1 = f1()
v2 = f3()
v3 = f3()
v4 = 0
for v5 in range(v1):
    if v2[v5] - v3[v5] >= 0:
        v4 += v2[v5] - v3[v5]
print(v4)
