import sys, collections as cl, bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
v1 = 10 ** 9 + 7
v2 = sys.maxsize

def f1():
    return list(map(int, input().split()))

def f2():
    return map(int, input().split())

def f3():
    return int(input())

def f4(a1):
    v1 = []
    v2 = a1[0]
    v3 = 1
    for v4 in range(len(a1) - 1):
        if v2 != a1[v4 + 1]:
            v1.append([v2, v3])
            v2 = a1[v4 + 1]
            v3 = 1
        else:
            v3 += 1
    v1.append([v2, v3])
    return v1

def f5(a1):
    return ' '.join(map(str, a1))

def f6(a1):
    return max(map(max, a1))

def f7(a1, a2):
    v1 = bs.bisect_left(a2, a1)
    if v1 != len(a2) and a2[v1] == a1:
        return True
    else:
        return False
'\ndef nibu(x,n,r):\n    ll = 0\n    rr = r\n    while True:\n        mid = (ll+rr)//2\n\n    if rr == mid:\n        return ll\n    if (ここに評価入れる):\n        rr = mid\n    else:\n        ll = mid+1\n'
v1 = 10 ** 9 + 7
v3 = 10 ** 5 * 2

def f8(a1, a2):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return g1[a1] * g2[a2] * g2[a1 - a2] % v1

def f9(a1, a2):
    if a2 < 0 or a2 > a1:
        return 0
    return g1[a1] * g2[a1 - a2] % v1
v4 = [1, 1]
v5 = [1, 1]
v6 = [0, 1]
for v7 in range(2, v3 + 1):
    v4.append(v4[-1] * v7 % v1)
    v6.append(-v6[v1 % v7] * (v1 // v7) % v1)
    v5.append(v5[-1] * v6[-1] % v1)
import fractions
from functools import reduce

def f10(*a1):
    return reduce(fractions.gcd, a1)

def f11(a1):
    return reduce(fractions.gcd, a1)

def f12(a1, a2):
    return a1 * a2 // fractions.gcd(a1, a2)

def f13(*a1):
    return reduce(f12, a1, 1)

def f14(a1):
    return reduce(f12, a1, 1)
v8, v9, v10 = f2()
v11 = str(v8)[::-1]
v12 = 1
v13 = [[1] for v7 in range(10)]
for v7 in range(9):
    v13[0].append(v13[0][-1] * 2)
for v7 in range(1, 10):
    for v14 in range(9):
        if v14 == 0:
            v13[v7].append(v13[v7 - 1][-1] * v13[v7 - 1][1] % v1)
        else:
            v13[v7].append(v13[v7][-1] * v13[v7][1] % v1)
for v7 in range(len(v11)):
    if v7 == 0:
        v12 *= v13[v7][int(v11[v7])]
    else:
        v12 = v12 * v13[v7][int(v11[v7])] % v1
        v12 = v12 % v1
v15 = 1
v16 = 1
for v7 in range(min(v9, v8 - v9)):
    v15 *= v8 - v7
    v15 %= v1
    if v7 == min(v9, v8 - v9) - 1:
        v15 *= v5[v7 + 1]
        v15 %= v1
for v7 in range(min(v10, v8 - v10)):
    v16 *= v8 - v7
    v16 %= v1
    if v7 == min(v10, v8 - v10) - 1:
        v16 *= v5[v7 + 1]
        v16 %= v1
print((v12 - v15 - v16 - 1) % v1)
