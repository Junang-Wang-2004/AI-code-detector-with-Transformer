import sys
v1 = 10 ** 9 + 7

def f1():
    return list(map(int, sys.stdin.readline().split()))
v2, v3, v4 = f1()
v5 = pow(2, v2, v1) - 1

def f2(a1, a2, a3):
    v1 = 1
    v2 = 1
    for v3 in range(a2):
        v1 = v1 * (a1 - v3) % a3
        v2 = v2 * (v3 + 1) % a3
    return v1 * pow(v2, a3 - 2, a3) % a3
v5 -= f2(v2, v3, v1)
v5 -= f2(v2, v4, v1)
if v2 >= v3:
    v5 += f2(v2, v3, v1)
if v2 >= v4:
    v5 += f2(v2, v4, v1)
v5 %= v1
print(v5)
