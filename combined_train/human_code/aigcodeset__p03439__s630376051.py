import sys, os
from collections import defaultdict, deque
from fractions import gcd
from math import ceil, floor
sys.setrecursionlimit(10 ** 6)
v1 = sys.stdout.write
v2 = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0

def f1(a1=sys.stdin.readline):
    input = lambda: a1().rstrip()
    v1 = lambda: list(map(int, input().split()))
    v2 = lambda: int(input())
    v3 = lambda x: [v1() for v4 in range(x)]
    v5 = lambda c: print('Yes') if c else print('No')
    v6 = 10 ** 9 + 7
    v7 = v2()
    v8 = {'Vacant': 0, 'Male': 1, 'Female': 2}
    print(0, flush=True)
    v9 = v8[input()]
    if v9 == 0:
        return
    print(v7 - 1, flush=True)
    v10 = v8[input()]
    if v10 == 0:
        return
    v11 = 0
    v12 = v7 - 1
    while v12 - v11 > 1:
        v13 = (v11 + v12) // 2
        print(v13, flush=True)
        v14 = v8[input()]
        if v14 == 0:
            return
        if (v13 - v11) % 2 == 1:
            if v9 == v14:
                v12 = v13
                v10 = v14
            else:
                v11 = v13
                v9 = v14
        elif v14 != v9:
            v12 = v13
            v10 = v14
        else:
            v11 = v13
            v9 = v14
    print(-1)
if __name__ == '__main__':
    f1()
