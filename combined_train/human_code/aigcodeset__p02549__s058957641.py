import math
import sys
import os
sys.setrecursionlimit(10 ** 7)

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    return int(f1())

def f3():
    return list(f1().split())

def f4():
    return list(map(int, f3()))
if os.getenv('LOCAL'):
    v1 = v2 = os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    sys.stdin = open(v1, 'r')
v3 = float('inf')
v4 = 998244353
v5, v6 = f4()
v7 = [f4() for v8 in range(v6)]
v9 = [0] * (v5 + 1)
v10 = [0] * (v5 + 1)
v9[1] = 1
v10[1] = 1
for v11 in range(2, v5 + 1):
    for v12 in range(v6):
        v13, v14 = v7[v12]
        v15 = max(0, v11 - v14 - 1)
        v16 = max(0, v11 - v13)
        v9[v11] += v10[v16] - v10[v15]
        v9[v11] %= v4
    v10[v11] = (v10[v11 - 1] + v9[v11]) % v4
v17 = v9[v5]
print(v17)
