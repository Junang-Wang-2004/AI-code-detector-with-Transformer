from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def f1():
    return list(map(int, sys.stdin.readline().split()))

def f2():
    return int(sys.stdin.readline())

def f3():
    return list(map(list, sys.stdin.readline().split()))

def f4():
    return list(sys.stdin.readline())[:-1]

def f5(a1):
    v1 = [None for v2 in range(a1)]
    for v2 in range(a1):
        v1[v2] = f2()
    return v1

def f6(a1):
    v1 = [None for v2 in range(a1)]
    for v2 in range(a1):
        v1[v2] = f1()
    return v1

def f7(a1):
    v1 = [None for v2 in range(a1)]
    for v2 in range(a1):
        v1[v2] = f4()
    return v1

def f8(a1):
    v1 = [None for v2 in range(a1)]
    for v2 in range(a1):
        v1[v2] = f7()
    return v1
v1 = 1000000007

def f9():
    v1, v2 = f1()
    print(math.ceil((v1 + v2) / 2))

def f10():
    v1 = f4()
    v2 = f4()
    v1.sort()
    v2.sort()
    v2 = v2[::-1]
    v3 = [v1, v2]
    v3.sort()
    if v1 == v2:
        print('No')
    elif v3[0] == v1:
        print('Yes')
    else:
        print('No')

def f11():
    v1 = f2()
    v2 = defaultdict(int)
    v3 = f1()
    for v4 in v3:
        v2[v4] += 1
    v5 = 0
    for v4 in v2.keys():
        if v4 <= v2[v4]:
            v5 += v2[v4] - v4
        else:
            v5 += v2[v4]
    print(v5)

def f12():
    v1 = input().split('T')
    v2, v3 = f1()
    v4, v5 = [0, 0]
    v6 = len(v1)
    v7 = [-1 for v8 in range(17000)]
    v9 = [-1 for v8 in range(17000)]
    v7[len(v1[0]) + 8000] = 1
    v9[8000] = 0
    v10, v11 = [1, 0]
    v12 = deque()
    for v8 in range(1, v6):
        if v8 % 2 == 0:
            v13 = len(v1[v8])
            if v13 > 0:
                for v14 in range(17000):
                    if v7[v14] == v10:
                        v12.append(v14)
                v10 += 1
                while v12:
                    v14 = v12.pop()
                    if v14 + v13 < 17000:
                        v7[v14 + v13] = min(v10, v7[v14] + 1)
                    if v14 - v13 >= 0:
                        v7[v14 - v13] = min(v10, v7[v14] + 1)
    for v8 in range(1, v6):
        if v8 % 2 == 1:
            v13 = len(v1[v8])
            if v13 > 0:
                for v14 in range(17000):
                    if v9[v14] == v11:
                        v12.append(v14)
                v11 += 1
                while v12:
                    v14 = v12.pop()
                    if v14 + v13 < 17000:
                        v9[v14 + v13] = min(v11, v9[v14] + 1)
                    if v14 - v13 >= 0:
                        v9[v14 - v13] = min(v11, v9[v14] + 1)
    if v7[v2 + 8000] == v10 and v9[v3 + 8000] == v11:
        print('Yes')
    else:
        print('No')

def f13():
    return

def f14():
    return

def f15():
    return

def f16():
    return
if __name__ == '__main__':
    f12()
