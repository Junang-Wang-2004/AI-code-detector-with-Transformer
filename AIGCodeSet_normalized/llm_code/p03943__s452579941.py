import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time
sys.setrecursionlimit(10 ** 7)
v1 = 10 ** 20
v2 = 10 ** 9 + 7

def f1():
    return list(map(int, input().split()))

def f2():
    return int(input())

def f3():
    return input()

def f4():
    v1, v2, v3 = f1()
    if (v1 + v2 + v3) % 2 == 0:
        return 'Yes'
    return 'No'
print(f4())
