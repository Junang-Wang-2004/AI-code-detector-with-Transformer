from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime
sys.setrecursionlimit(10 ** 8)
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = 10 ** (-7)

def f1():
    return list(map(int, input().split()))

def f2():
    return list(input().split())
v4, v5 = f1()
if v4 * v5 % 2 == 1:
    print('Yes')
else:
    print('No')
