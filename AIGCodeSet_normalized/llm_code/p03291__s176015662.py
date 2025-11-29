v1 = input()
v2 = len(v1)
v3 = 10 ** 9 + 7
import sys
sys.setrecursionlimit(200000)
from functools import lru_cache

@lru_cache(maxsize=None)
def f1(a1, a2):
    if a1 == v2:
        if a2 == 3:
            return 1
        else:
            return 0
    elif v1[a1] == 'A' and a2 == 0:
        return (f1(a1 + 1, a2 + 1) + f1(a1 + 1, a2)) % v3
    elif v1[a1] == 'B' and a2 == 1:
        return (f1(a1 + 1, a2 + 1) + f1(a1 + 1, a2)) % v3
    elif v1[a1] == 'C' and a2 == 2:
        return (f1(a1 + 1, a2 + 1) + f1(a1 + 1, a2)) % v3
    elif v1[a1] == '?' and a2 != 3:
        return (f1(a1 + 1, a2 + 1) + 3 * f1(a1 + 1, a2)) % v3
    elif v1[a1] == '?':
        return 3 * f1(a1 + 1, a2) % v3
    else:
        return f1(a1 + 1, a2) % v3
print(f1(0, 0) % v3)
