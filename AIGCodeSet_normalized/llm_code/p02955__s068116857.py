import sys
from math import sqrt
from collections import deque

def f1():
    return sys.stdin.readline().strip()

def f2(a1, a2, a3):
    return [[a3] * a2 for v1 in range(a1)]

def f3(a1, a2, a3, a4):
    return [[[a4] * a3 for v1 in range(a2)] for v2 in range(a1)]

def f4(a1, a2=1):
    return int(-(-a1 // a2))

def f5():
    return int(f1())

def f6():
    return map(int, f1().split())

def f7():
    return list(map(int, f1().split()))

def f8():
    print('Yes')

def f9():
    print('No')

def f10():
    print('YES')

def f11():
    print('NO')
sys.setrecursionlimit(10 ** 9)
v1 = float('inf')
v2 = 10 ** 9 + 7
v3, v4 = f6()
v5 = f7()
v6 = sum(v5)

def f12(a1: int) -> set:
    """ 約数の列挙・個数 """
    v1 = {1, a1}
    for v2 in range(2, int(sqrt(a1)) + 1):
        if a1 % v2 == 0:
            v1.add(v2)
            v1.add(a1 // v2)
    return v1
v7 = sorted(f12(v6), reverse=True)
for v8 in v7:
    v9 = []
    for v10 in range(v3):
        if v5[v10] % v8 != 0:
            v9.append(v5[v10] % v8)
    v9.sort()
    v9 = deque(v9)
    v11 = 0
    while len(v9):
        v12 = v9[0] % v8
        v13 = v8 - v9[-1] % v8
        if v12 > v13:
            v9[0] -= v13
            v9.pop()
            v11 += v13
        elif v12 < v13:
            v9[-1] -= v12
            v9.popleft()
            v11 += v12
        else:
            v9.pop()
            v9.popleft()
            v11 += v12
    if v11 <= v4:
        print(v8)
        exit()
