import sys
from math import gcd
from functools import reduce
v1 = sys.stdin.read
v2 = sys.stdin.readline
v3 = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
v4 = 1 << 60
v5 = 1000000007

def f1():
    v1, *v2 = map(int, v1().split())
    print(reduce(gcd, v2))
    return
if __name__ == '__main__':
    f1()
