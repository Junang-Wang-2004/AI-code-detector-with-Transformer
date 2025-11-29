import math
import queue
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
v1 = stdin.readline
setrecursionlimit(10 ** 7)

def f1():
    v1 = int(v1())
    v2 = []
    v3 = []
    for v4 in range(v1):
        v5, v6 = map(int, v1().split())
        v2.append(v5)
        v3.append(v6)
    v7 = 0
    for v4 in range(v1):
        v5 = v2[v1 - 1 - v4]
        v6 = v3[v1 - 1 - v4]
        v8 = v6 - (v5 + v7 - 1) % v6 - 1
        v7 += v8
    print(v7)
    return
if __name__ == '__main__':
    f1()
