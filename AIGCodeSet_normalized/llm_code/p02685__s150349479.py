v1 = 998244353

def f1(a1, a2):
    v1 = 1
    while a2 > 0:
        if a2 % 2 == 1:
            v1 = v1 * a1 % v1
        a1 = a1 * a1 % v1
        a2 //= 2
    return v1

def f2(a1, a2):
    if a2 > a1 - a2:
        a2 = a1 - a2
    v2 = 1
    for v3 in range(a2):
        v2 = v2 * (a1 - v3) % v1
        v2 = v2 * f1(v3 + 1, v1 - 2) % v1
    return v2

def f3(a1, a2, a3):
    v1 = 0
    for v2 in range(a3 + 1):
        v1 = (v1 + f1(a2, v2 + 1) * f2(a1 - 1, v2) * f1(a2 - 1, a1 - v2)) % v1
    return v1
v2, v3, v4 = map(int, input().split())
print(f3(v2, v3, v4))
