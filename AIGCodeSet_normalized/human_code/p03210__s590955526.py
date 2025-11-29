def f1():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    v1 = int(input())
    if v1 in [3, 5, 7]:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    f1()
