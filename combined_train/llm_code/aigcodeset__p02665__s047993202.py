import sys
import math
sys.setrecursionlimit(10 ** 5 + 10)

def f1():
    return sys.stdin.readline().strip()

def f2():
    v1 = int(f1())
    v2 = list(map(int, f1().split()))
    v3 = [0] * (v1 + 1)
    v3[v1] = (v2[v1], v2[v1])
    for v4 in reversed(range(1, v1 + 1)):
        v3[v4 - 1] = (max(math.ceil(v3[v4][0] / 2) + v2[v4 - 1], 1), v3[v4][1] + v2[v4 - 1])
    if 1 not in range(v3[0][0], v3[0][1] + 1):
        print(-1)
    else:
        v5 = [0] * (v1 + 1)
        v5[0] = 1
        v6 = 1
        for v4 in range(v1):
            v5[v4 + 1] = min((v5[v4] - v2[v4]) * 2, v3[v4 + 1][1])
        print(sum(v5))
f2()
