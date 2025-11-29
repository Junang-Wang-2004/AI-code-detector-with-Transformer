from collections import defaultdict
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
'\nn = I()\ns = SR(n)\nfor i in range(n):\n    for j in range(len(s[i])):\n        while s[i][j] in s[i][:j]:\n            s[i][j] = "0"+s[i][j]\nans = set(s[0])\nfor i in range(1,n):\n    ans &= set(s[i])\nans = sorted(list(ans))\nif len(ans) == 0:print()\nelse:\n    for i in range(len(ans)):\n        ans[i] = ans[i][-1]\n    ans.sort()\n    for i in range(len(ans)-1):\n        print(ans[i],end = "")\n    print(ans[-1])\n'
v2, v3 = f1()
v4 = [v2 - 1]
v5 = [v3 - 1]
v6 = v2 - 1
v7 = v3 - 1
while v6 > 2:
    v6 -= 2
    v4.append(v4[-1] + v6)
while v7 > 2:
    v7 -= 2
    v5.append(v5[-1] + v7)
v8 = len(v4)
v9 = len(v5)
for v10 in range(v8):
    if v10 or v6 == 2:
        v4.append(v4[v8 - v10 - 1])
for v10 in range(v9):
    if v10 or v7 == 2:
        v5.append(v5[v9 - v10 - 1])
v11, v12 = f6(2)
v13 = 0
v14 = 0
for v10 in range(v2 - 1):
    v13 += v4[v10] * (v11[v10 + 1] - v11[v10]) % v1
    v13 %= v1
for v10 in range(v3 - 1):
    v14 += v5[v10] * (v12[v10 + 1] - v12[v10]) % v1
    v14 %= v1
v15 = v13 * v14 % v1
print(v15)
