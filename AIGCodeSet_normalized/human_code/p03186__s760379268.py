def f1():
    return [int(j) for v1 in input().split()]
from collections import Counter
v1, v2, v3 = f1()
if v1 + v2 >= v3:
    print(v2 + v3)
else:
    v4 = 0
    v4 = 2 * v2
    v3 -= v2
    if v3 <= v1 + 1:
        v4 += v3
    else:
        v4 += v1 + 1
    print(v4)
