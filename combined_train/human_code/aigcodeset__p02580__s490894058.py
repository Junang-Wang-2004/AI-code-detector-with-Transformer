import sys
from io import StringIO
import unittest

def f1(a1):
    print('Yes' if a1 == 1 else 'No')
    return

def f2():
    v1 = sys.stdin.readline
    v2, v3, v4 = map(int, v1().rstrip().split())
    v5 = [0] * v2
    v6 = [0] * v3
    v7 = [0] * v4
    v8 = [0] * v4
    for v9 in range(v4):
        v10, v11 = map(int, v1().rstrip().split())
        v10 -= 1
        v11 -= 1
        v5[v10] += 1
        v6[v11] += 1
        v7[v9] = v10
        v8[v9] = v11
    v12 = max(v6)
    v13 = max(v5)
    v14 = v6.count(v12)
    v15 = v5.count(v13)
    v16 = v14 * v15
    for v9 in range(v4):
        v10 = v7[v9]
        v11 = v8[v9]
        v17 = False
        if v5[v10] == v13 and v6[v11] == v12:
            v16 -= 1
    if v16 > 0:
        print(v12 + v13)
    else:
        print(v12 + v13 - 1)
    return
if 'doTest' not in globals():
    f2()
    sys.exit()
