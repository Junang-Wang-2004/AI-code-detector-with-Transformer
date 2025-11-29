from functools import reduce
import math

def f1(a1, a2):
    if a1 % a2 == 0:
        return a2
    else:
        return f1(a2, a1 % a2)

def f2(a1):
    v1 = []
    v2 = a1
    for v3 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v2 % v3 == 0:
            v4 = 0
            while v2 % v3 == 0:
                v4 += 1
                v2 //= v3
            v1.append(v3)
    if v2 != 1:
        v1.append(v2)
    if v1 == []:
        v1.append(a1)
    return v1

def f3(a1, a2):
    v1 = {}
    for v2 in range(a1):
        v3 = f2(a2[v2])
        for v4 in v3:
            if v4 == 1:
                pass
            elif v4 not in v1:
                v1[v4] = 1
            else:
                return True
    return False
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = reduce(math.gcd, v2)
if v3 != 1:
    print('not coprime')
elif f3(v1, v2):
    print('setwise coprime')
else:
    print('pairwise coprime')
