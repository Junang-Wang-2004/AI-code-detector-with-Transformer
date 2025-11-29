import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations, combinations, accumulate
from operator import itemgetter
from bisect import bisect_left, bisect
from heapq import heappop, heappush, heapify
from math import ceil, floor, sqrt, factorial
from copy import deepcopy

def f1():
    v1 = int(input()) % (10 ** 9 + 7)
    v2 = 0
    v3 = 10 ** v1 - 2 * 9 ** v1 + 8 ** v1
    print(v3 % (10 ** 9 + 7))
if __name__ == '__main__':
    f1()
