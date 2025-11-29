import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

def f1(a1, a2, a3, a4):
    if a4 == a2:
        return 1
    else:
        return (f1(a1, a2, a3, a4 + 1) + (0 if a1[a4] in a3 else f1(a1, a2, a3 + a1[a4], a4 + 1))) % (10 ** 9 + 7)
v1 = int(input())
v2 = list(input().strip())
print(f1(v2, v1, '', 0) - 1)
