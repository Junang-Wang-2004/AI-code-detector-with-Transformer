import math
import queue
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
v1 = stdin.readline
setrecursionlimit(10 ** 7)

def f1():
    v1, v2 = map(int, v1().split())
    if v1 < v2:
        v3 = v2 - v1
    else:
        v3 = v1 - v2 + 2
    if v1 * v2 < 0:
        v3 = min(v3, abs(abs(v1) - abs(v2)) + 1)
    elif v1 == 0:
        if v2 < 0:
            v3 = abs(v2) + 1
    elif v2 == 0:
        if v1 > 0:
            v3 = v1 + 1
    print(v3)
    return
if __name__ == '__main__':
    f1()
