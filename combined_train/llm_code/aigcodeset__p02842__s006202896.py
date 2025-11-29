import sys
from collections import deque
import numpy as np
import math
sys.setrecursionlimit(10 ** 6)

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    return map(str, sys.stdin.readline().rstrip().split())

def f3():
    return int(sys.stdin.readline().rstrip())

def f4():
    return map(int, sys.stdin.readline().rstrip().split())

def f5():
    v1 = math.ceil(n / 1.08)
    if math.floor(v1 * 1.08) == n:
        print(v1)
    else:
        print(':(')
    return
if __name__ == '__main__':
    v1 = f3()
    f5()
