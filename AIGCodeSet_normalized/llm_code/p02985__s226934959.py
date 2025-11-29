from functools import reduce
import math
from collections import defaultdict
v1 = -10 ** 9
v2 = 10 ** 9 + 7
from math import factorial

def f1():
    v1, v2 = [int(a) for v3 in input().split()]
    v4 = [[int(v3) for v3 in input().split()] for v5 in range(v1 - 1)]
    v6 = defaultdict(lambda: [])
    for v7, v8 in v4:
        v9 = v6[v7]
        v9.append(v8)
        v6[v7] = v9
        v9 = v6[v8]
        v9.append(v7)
        v6[v8] = v9

    def parsetree(a1, a2):
        v1 = []
        for v2 in v6[a2]:
            if v2 == a1:
                continue
            v3 = parsetree(a2, v2)
            v1.append(v3)
        return v1
    v10 = parsetree(None, 1)
    if len(v10) > v2 - 1:
        print(0)
        return

    def c(a1, a2):
        v1 = 1
        for v2 in range(a2):
            v1 = v1 * (a1 - v2) % v2
        return v1

    def f(a1):
        v1 = len(a1)
        v2 = c(v2 - 2, v1)
        for v3 in a1:
            v4 = f(v3) % v2
            v2 = v2 * v4 % v2
        return v2
    try:
        v11 = v2 * c(v2 - 1, len(v10))
        for v12 in v10:
            v9 = f(v12) % v2
            v11 = v11 * v9 % v2
    except:
        print(0)
        return
    print(v11)
if __name__ == '__main__':
    f1()
