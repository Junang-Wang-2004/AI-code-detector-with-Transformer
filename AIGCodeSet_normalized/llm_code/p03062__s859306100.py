import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(1000000)
v1 = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
v2 = lambda: int(input())
v3 = lambda: map(int, input().split())
v4 = lambda: list(v3())
v5 = lambda: input()

def f1():
    v1 = v2()
    v2 = v4()
    v3 = 0
    for v4 in range(v1):
        v3 += abs(v2[v4])
    for v4 in range(v1 - 1):
        if v2[v4] * v2[v4 + 1] < 0:
            v3 -= 2 * min(abs(v2[v4]), abs(v2[v4 + 1]))
    print(v3)
if __name__ == '__main__':
    f1()
