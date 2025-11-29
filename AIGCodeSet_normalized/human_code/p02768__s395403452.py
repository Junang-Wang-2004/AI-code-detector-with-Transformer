def f1():
    return input()

def f2():
    return input().split()

def f3(a1):
    return [input() for v1 in range(a1)]

def f4(a1):
    return [input().split() for v1 in range(a1)]

def f5(a1):
    return [[x for v1 in s] for v2 in f3(a1)]

def f6():
    return int(input())

def f7():
    return [int(x) for v1 in input().split()]

def f8(a1):
    return [int(input()) for v1 in range(a1)]

def f9(a1):
    return [[int(x) for v1 in input().split()] for v2 in range(a1)]

def f10(a1):
    return [tuple((int(x) for v1 in input().split())) for v2 in range(a1)]

def f11(a1, a2='Yes', a3='No'):
    print(a2 if a1 else a3)
v1, v2, v3 = f7()

def f12(a1, a2):
    v1 = 1
    v2 = 10 ** 9 + 7
    for v3 in range(a1 - a2 + 1, a1 + 1):
        v1 *= v3
        v1 %= v2
    for v3 in range(1, a2 + 1):
        v1 *= pow(v3, v2 - 2, v2)
        v1 %= v2
    return v1
v4 = 10 ** 9 + 7
v5 = f12(v1, v2)
v6 = f12(v1, v3)
v7 = pow(2, v1, v4) - v5 - v6 - 1
print(v7 % v4)
