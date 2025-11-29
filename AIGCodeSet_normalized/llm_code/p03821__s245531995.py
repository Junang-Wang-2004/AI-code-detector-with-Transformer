import numpy as np
import math
import collections
import fractions
import itertools

def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return list(map(int, input().split()))

def f4():
    v1 = int(input())
    v2 = 0
    for v3 in range(v1):
        v4, v5 = f2()
        v2 += (v5 - v4 % v5) % v5
    print(v2)
    return 0
if __name__ == '__main__':
    f4()
