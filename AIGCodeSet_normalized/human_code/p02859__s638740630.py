from collections import deque
from collections import Counter
from itertools import product, permutations, combinations
from operator import itemgetter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right, bisect
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi, factorial
import sys
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
v4 = float('inf')

def f1():
    v1 = int(v1())
    print(v1 ** 2)
if __name__ == '__main__':
    f1()
