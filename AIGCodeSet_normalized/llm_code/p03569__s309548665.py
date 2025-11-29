from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time

def f1():
    return int(f9())

def f2():
    return f9()

def f3():
    return map(int, f9().split())

def f4():
    return map(str, f9().split())

def f5():
    return [int(i) for v1 in f9().split()]

def f6():
    return [int(i) - 1 for v1 in f9().split()]

def f7():
    return [ord(i) - 97 for v1 in f9()]

def f8(a1):
    return chr(a1 + 97)

def f9():
    return sys.stdin.readline().rstrip()

def f10(*a1, a2='\n'):
    if show_flg:
        print(*a1, end=a2)
v1 = {False: 'No', True: 'Yes'}
v2 = {False: 'NO', True: 'YES'}
v3 = 10 ** 9 + 7
v4 = float('inf')
v5 = 10 ** 10
v6 = string.ascii_lowercase
v7 = string.ascii_uppercase
v8 = time.time()
sys.setrecursionlimit(10 ** 6)
v9 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
v10 = False

def f11(a1, a2):
    if int(a1 / a2):
        return f11(int(a1 / a2), a2) + str(a1 % a2)
    return str(a1 % a2)

def f12():
    v1 = f1()
    for v2 in range(2, 10000 + 1):
        if str(v2) == f11(v1, v2):
            print(v2)
            return
    print(-1)
if __name__ == '__main__':
    f12()
