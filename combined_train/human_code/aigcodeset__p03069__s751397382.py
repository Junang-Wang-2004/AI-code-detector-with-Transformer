import sys
input = sys.stdin.readline
import math
import bisect
import heapq
from collections import defaultdict
from collections import deque
from collections import Counter
from functools import lru_cache
v1 = 10 ** 9 + 7
v2 = float('inf')
v3 = 'abcdefghijklmnopqrstuvwxyz'

def f1():
    return int(input().strip())

def f2():
    return input().strip()

def f3():
    return list(map(int, input().split()))

def f4():
    return list(map(str, input().split()))

def f5(a1):
    return list((int(input()) for v1 in range(a1)))

def f6(a1):
    return list((input().strip() for v1 in range(a1)))

def f7(a1):
    return [list(map(int, input().split())) for v1 in range(a1)]

def f8(a1):
    return [list(map(str, input().split())) for v1 in range(a1)]

def f9(a1):
    print(a1)
    return

def f10():
    print('Yes')
    return

def f11():
    print('No')
    return

def f12():
    exit()

def f13(a1):
    print(a1)
    exit()

def f14():
    print('Yes')
    exit()

def f15():
    print('No')
    exit()

def f16(a1):
    return defaultdict(a1)

def f17(a1):
    return pow(a1, v1 - 2, v1)
v4 = []

def f18(a1):
    if len(v4) > a1:
        return v4[a1]
    if len(v4) == 0:
        v4.append(1)
    while len(v4) <= a1:
        v4.append(v4[-1] * len(v4) % v1)
    return v4[a1]
v5 = []

def f19(a1):
    if len(v5) > a1:
        return v5[a1]
    if len(v5) == 0:
        v5.append(1)
    while len(v5) <= a1:
        v5.append(v5[-1] * pow(len(v5), v1 - 2, v1) % v1)
    return v5[a1]

def f20(a1, a2):
    if a1 == a2:
        return 1
    if a1 < a2 or a2 < 0:
        return 0
    v1 = 1
    v1 = v1 * f18(a1) % v1
    v1 = v1 * f19(a2) % v1
    v1 = v1 * f19(a1 - a2) % v1
    return v1

def f21(a1):
    v1 = []
    v2 = a1
    for v3 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v2 % v3 == 0:
            v4 = 0
            while v2 % v3 == 0:
                v4 += 1
                v2 //= v3
            v1.append([v3, v4])
    if v2 != 1:
        v1.append([v2, 1])
    if v1 == []:
        v1.append([a1, 1])
    return v1

def f22(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    v1.sort()
    return v1

def f23(a1):
    max = int(math.sqrt(a1))
    v1 = [i for v2 in range(2, a1 + 1)]
    v3 = []
    while v1[0] <= max:
        v3.append(v1[0])
        v4 = v1[0]
        v1 = [v2 for v2 in v1 if v2 % v4 != 0]
    v3.extend(v1)
    return v3

def f24(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f25(a1, a2):
    return a1 * a2 // f24(a1, a2)

def f26(a1):
    v1 = 0
    while a1:
        a1 &= a1 - 1
        v1 += 1
    return v1

def f27(a1, a2):
    if a1 // a2:
        return f27(a1 // a2, a2) + [a1 % a2]
    return [a1 % a2]

def f28(a1, a2):
    return sum((int(str(a1)[-i - 1]) * a2 ** i for v1 in range(len(str(a1)))))

def f29(a1, a2):
    v1 = 0
    while a1 >= a2:
        a1 //= a2
        v1 += 1
    return v1
v6 = f1()
v7 = v7()
if v7[0] == '.':
    v8 = [1]
else:
    v8 = [0]
for v9 in v7[1:]:
    if v9 == '.':
        v8.append(v8[-1] + 1)
    else:
        v8.append(v8[-1])
v10 = v8[-1]
for v11 in range(v6):
    v10 = min(v10, v11 + 1 - v8[v11] + (v6 - v11 - 1) - (v6 - v11 - 1 - (v8[-1] - v8[v11])))
print(v10)
