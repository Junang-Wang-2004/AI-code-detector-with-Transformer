import functools
import os
import sys
sys.setrecursionlimit(10000)
v1 = float('inf')

def f1():
    return int(input())

def f2():
    return float(input())

def f3():
    return input()

def f4():
    return list(map(int, input().split()))

def f5():
    return list(map(float, input().split()))

def f6():
    return input().split()

def f7(a1):
    return [f1() for v1 in range(a1)]

def f8(a1):
    return [f2() for v1 in range(a1)]

def f9(a1):
    return [f3() for v1 in range(a1)]

def f10(a1):
    return [f4() for v1 in range(a1)]

def f11(a1):
    return [f5() for v1 in range(a1)]

def f12(a1):
    return [f6() for v1 in range(a1)]

def f13(a1):
    print('Yes' if a1 else 'No')

def f14(a1):
    print('YES' if a1 else 'NO')

def f15(a1):
    print('yes' if a1 else 'no')
v2, v3, v4 = f6()
if v3 == '+':
    print(int(v2) + int(v4))
else:
    print(int(v2) - int(v4))
