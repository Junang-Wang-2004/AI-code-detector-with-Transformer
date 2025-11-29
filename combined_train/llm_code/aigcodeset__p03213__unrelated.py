import math

def f1(a1):
    v1 = 0
    for v2 in range(1, int(math.sqrt(a1)) + 1):
        if a1 % v2 == 0:
            v1 += 1
            if v2 != a1 // v2:
                v1 += 1
    return v1

def f2(a1):
    v1 = 1
    for v2 in range(1, a1 + 1):
        v1 *= v2
    return v1

def f3(a1):
    v1 = f2(a1)
    v2 = 0
    for v3 in range(1, v1 + 1):
        if f1(v3) == 75:
            if v1 % v3 == 0:
                v2 += 1
    return v2
v1 = int(input())
print(f3(v1))
