import sys
v1 = 10 ** 9 + 7

def f1(a1):
    v1 = [1] * (a1 + 1)
    for v2 in range(1, a1 + 1):
        v1[v2] = v1[v2 - 1] * v2 % v1
    return v1

def f2(a1, a2):
    v1 = 1
    while a2 > 0:
        if a2 % 2 == 1:
            v1 = v1 * a1 % v1
        a1 = a1 * a1 % v1
        a2 //= 2
    return v1

def f3(a1, a2):
    v1 = f1(a1)
    return v1[a1] * f2(v1[a2], v1 - 2) * f2(v1[a1 - a2], v1 - 2) % v1

def f4(a1, a2):
    if a2 == 0:
        return 1
    if a2 > a1 * (a1 - 1) // 2:
        return 0
    v1 = 0
    for v2 in range(1, a1 + 1):
        v1 = (v1 + f3(a1, v2) * f4(a1 - v2, a2 - v2 * (v2 - 1) // 2)) % v1
    return v1
v2, v3 = map(int, sys.stdin.readline().split())
print(f4(v2, v3))
