import math
import os
import sys
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
v1 = float('inf')
v2 = 10 ** 18
v3 = 10 ** 9 + 7

def f1(a1):
    """
    n の約数をリストで返す
    :param int n:
    :rtype: list of int
    """
    v1 = []
    for v2 in range(1, int(math.sqrt(a1)) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if a1 // v2 != v2:
                v1.append(a1 // v2)
    return v1

def f2(a1):
    """
    素因数分解
    :param int n:
    :rtype: list of int
    """
    if a1 <= 1:
        return []
    v1 = []
    while a1 > 2 and a1 % 2 == 0:
        v1.append(2)
        a1 //= 2
    v3 = 3
    while v3 <= math.sqrt(a1):
        if a1 % v3 == 0:
            v1.append(v3)
            a1 //= v3
        else:
            v3 += 2
    v1.append(a1)
    return v1
v4, v5 = list(map(int, sys.stdin.readline().split()))
v6 = set(f2(v4))
v7 = set(f2(v5))
v8 = len(v6 & v7) + 1
print(v8)
