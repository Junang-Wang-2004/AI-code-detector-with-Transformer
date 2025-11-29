import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (v1 + 1)
v3[0] = 1
if v2[0] != 0:
    if v1 != 0:
        print(-1)
        exit()
    else:
        print(1)
        exit()
if v2[v1] == 0:
    print(-1)
    exit()
v3[v1] = v2[v1]
from functools import lru_cache

@lru_cache(None)
def f1(a1, a2):
    if a1 == 0:
        if v3[0] == 1:
            return True
        else:
            return False
    v1 = v2[a1] - -a2 // 2
    v3[a1] = v1
    if not f1(a1 - 1, a2):
        return False
    v2 = v2[a1] + a2
    v2 = min(v2, 2 ** a1)
    while v2 >= v2[a1] - -a2 // 2:
        if f1(a1 - 1, a2):
            v3[a1] = v2
            break
        v2 -= 1
    else:
        return False
    return True
v4 = f1(v1 - 1, v3[v1])
if v4:
    print(sum(v3))
else:
    print(-1)
