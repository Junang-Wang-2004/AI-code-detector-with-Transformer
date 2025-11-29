import sys
sys.setrecursionlimit(10 ** 8)

def f1():
    return int(sys.stdin.readline())

def f2():
    return map(int, sys.stdin.readline().split())

def f3():
    return list(map(int, sys.stdin.readline().split()))

def f4(a1):
    return [list(map(int, sys.stdin.readline().split())) for v1 in range(a1)]

def f5(a1, a2, a3):
    return [[a1] * a2 for v1 in range(a3)]

def f6(a1, a2, a3, a4):
    return [[[a1] * a2 for v1 in range(a3)] for v1 in range(a4)]
import bisect
v1 = f1()
v2 = sorted(f3())
v3 = (v2[-1], v2[0])
for v4 in range(v1 - 1):
    for v5 in range(v4 + 1, v1):
        if v3[0] * v3[1] < v2[v5] * v2[v4]:
            v3 = (v2[v5], v2[v4])
print(v3[0], v3[1])
