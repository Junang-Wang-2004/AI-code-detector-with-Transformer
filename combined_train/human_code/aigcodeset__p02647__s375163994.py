import sys
from itertools import accumulate

def f1():
    return sys.stdin.readline().strip()

def f2(a1, a2, a3):
    return [[a3] * a2 for v1 in range(a1)]

def f3(a1, a2, a3, a4):
    return [[[a4] * a3 for v1 in range(a2)] for v2 in range(a1)]

def f4(a1, a2, a3, a4, a5):
    return [[[[a5] * a4 for v1 in range(a3)] for v1 in range(a2)] for v2 in range(a1)]

def f5(a1, a2=1):
    return int(-(-a1 // a2))

def f6():
    return int(f1())

def f7():
    return map(int, f1().split())

def f8(a1=None):
    return list(f7()) if a1 is None else [f6() for v1 in range(a1)]

def f9():
    print('Yes')

def f10():
    print('No')

def f11():
    print('YES')

def f12():
    print('NO')
sys.setrecursionlimit(10 ** 9)
v1 = 10 ** 19
v2 = 10 ** 9 + 7
v3, v4 = f7()
v5 = f8()
v6 = v5[:]
for v7 in range(v4):
    v8 = [0] * (v3 + 1)
    for v9 in range(v3):
        v8[max(v9 - v6[v9], 0)] += 1
        v8[min(v9 + v6[v9] + 1, v3)] -= 1
    v8 = list(accumulate(v8))
    v6 = v8[:-1]
    if min(v6) == v3:
        break
print(*v6)
