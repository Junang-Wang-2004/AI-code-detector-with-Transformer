import math

def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f2(a1, a2):
    v1 = f1(a1, a2)
    return int(math.log2(v1)) + 1
v1, v2 = map(int, input().split())
print(f2(v1, v2))
