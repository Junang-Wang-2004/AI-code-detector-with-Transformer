import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 9)
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
v4 = v2()
v5 = v3()
v6 = 10 ** 17

@lru_cache(None)
def f1(a1, a2):
    if a1 >= v4:
        return -v6
    if v4 - a1 + 2 < 2 * a2:
        return -v6
    if a2 == 0:
        return 0
    elif a2 == 1:
        return max(v5[a1:])
    v1 = max(v5[a1] + f1(a1 + 2, a2 - 1), f1(a1 + 1, a2))
    return v1
v7 = f1(0, v4 // 2)
print(v7)
