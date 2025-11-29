import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
import bisect
import numpy as np
v1 = int(input())
if v1 % 10 in [2, 4, 5, 7, 9]:
    print('hon')
elif v1 % 10 in [0, 1, 6, 8]:
    print('pon')
elif v1 % 10 in [3]:
    print('bon')
