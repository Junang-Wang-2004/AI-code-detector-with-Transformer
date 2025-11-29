import sys
from math import ceil

def f1():
    return sys.stdin.readline().strip()

def f2():
    return int(f1())

def f3():
    return float(f1())

def f4():
    return f1().split()

def f5():
    return map(int, f4())

def f6():
    return list(f5())

def f7(a1, a2):
    v1 = a1 * a2
    while a1 != 0 and a2 != 0:
        if a1 > a2:
            a1 %= a2
        else:
            a2 %= a1
    return v1 // (a1 + a2)

def f8():
    v1 = 10 ** 9 + 7
    v2, v3 = f5()
    v4 = f6()
    v5 = f6()
    v6 = [1] * (v3 + 1)
    for v7 in v4:
        v8 = v6[:]
        v9 = 0
        for v10, v11 in enumerate(v5):
            v8[v10] = (v9 + v8[v10]) % v1
            if v7 == v11:
                v9 = (v9 + v6[v10]) % v1
        v8[-1] = (v9 + v8[-1]) % v1
        v6 = v8[:]
    print(v6[-1])
f8()
