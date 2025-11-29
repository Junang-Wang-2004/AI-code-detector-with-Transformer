from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, datetime
sys.setrecursionlimit(10 ** 8)
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = 10 ** (-7)

def f1():
    return int(input())

def f2():
    return list(map(int, input().split()))

def f3():
    return list(input().split())
v4 = [chr(i) for v5 in range(97, 97 + 26)]
v6 = f1()
v7 = f2()
v8 = v9 = 0
v10 = 0
v11 = 0
for v12 in range(v6):
    while v8 == v9:
        v11 += v10 - v12
        v10 += 1
        if v10 > v6:
            break
        v8 ^= v7[v10 - 1]
        v9 += v7[v10 - 1]
    else:
        v9 -= v7[v12]
        v8 ^= v7[v12]
        continue
    break
print(v11)
