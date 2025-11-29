import math
from collections import Counter
v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
v4 = []
for v5 in range(2, 2 * math.ceil(math.sqrt(v3))):
    while v3 % v5 == 0:
        v4.append(v5)
        v3 //= v5
if v3 > 1:
    v4.append(v3)

def f1(a1):
    if a1 == 1:
        return a1
    return a1 * f1(a1 - 1)

def f2(a1, a2):
    if a2 == 1:
        return a1
    return a1 * f2(a1 - 1, a2 - 1)

def f3(a1, a2):
    return f2(a1 + a2 - 1, a2) // f1(a2)
v6 = 1
for v7 in Counter(v4).values():
    v6 *= f3(v2, v7)
    v6 %= v1
print(v6)
