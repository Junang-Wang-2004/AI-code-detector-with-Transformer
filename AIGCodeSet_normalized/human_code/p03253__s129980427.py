import sys
from collections import Counter
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
v4, v5 = v3()
v6 = 10 ** 9 + 7

def f1(a1):
    v1 = []
    while a1 % 2 == 0:
        v1.append(2)
        a1 //= 2
    v3 = 3
    while v3 * v3 <= a1:
        if a1 % v3 == 0:
            v1.append(v3)
            a1 //= v3
        else:
            v3 += 2
    if a1 != 1:
        v1.append(a1)
    return v1

def f2(a1, a2, a3=10 ** 9 + 7):
    v1 = [1] * (a1 + 1)
    v2 = 1
    for v3 in range(1, a1 + 1):
        v2 = v2 * v3 % a3
        v1[v3] = v2
    v4 = v1[a1]
    v4 = v4 * pow(v1[a2], a3 - 2, a3) % a3
    v4 = v4 * pow(v1[a1 - a2], a3 - 2, a3) % a3
    return v4
v7 = f1(v5)
v8 = Counter(v7)
v9 = 1
for v10 in v8.values():
    v9 *= f2(v4 - 1 + v10, v10)
    v9 %= v6
print(v9)
