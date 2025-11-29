"""
自宅用PCでの解答
"""
import math
import itertools
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
v1 = stdin.readline
setrecursionlimit(10 ** 7)
v2 = 10 ** 9 + 7
v3 = 'abcdefghijklmnopqrstuvwxyz'

def f1():
    v1 = int(v1())
    if v1 >= 30:
        print('Yes')
    else:
        print('No')
    return None
if __name__ == '__main__':
    f1()
