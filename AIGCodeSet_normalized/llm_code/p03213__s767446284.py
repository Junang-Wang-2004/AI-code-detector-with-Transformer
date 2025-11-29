from collections import Counter as c
from itertools import combinations_with_replacement as p

def f1(a1):
    v1 = []
    for v2 in range(2, int(a1 ** 0.5) + 2):
        while a1 % v2 == 0:
            a1 //= v2
            v1.append(v2)
    if a1 != 1:
        v1.append(a1)
    return c(v1)
v1 = int(input())
v2 = c()
for v3 in range(1, v1 + 1):
    v2 += f1(v3)
v4 = lambda n, x: sum((1 for v3 in p(v2.values(), v1) if all(map(lambda x, y: x >= y, v3, x))))
print(v4(3, (2, 4, 4)) // 2 + v4(2, (2, 24)) + v4(2, (4, 14)) + v4(1, (74,)))
