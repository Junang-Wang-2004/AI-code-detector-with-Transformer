import math
v1 = 10 ** 9 + 7

def f1(a1, a2, a3):
    v1 = 1
    a1 %= a3
    while a2 > 0:
        if a2 % 2 == 1:
            v1 = v1 * a1 % a3
        a1 = a1 * a1 % a3
        a2 //= 2
    return v1

def f2(a1, a2):
    v1 = 0
    for v2 in range(1, a2 + 1):
        v1 = (v1 + f1(v2, a1, v1)) % v1
    return v1
v2, v3 = map(int, input().split())
print(f2(v2, v3))
