import sys, heapq, resource
from collections import deque, defaultdict
v1 = lambda x: sys.stdout.write(x)
v2 = lambda: int(input())
v3 = lambda: list(map(int, input().split()))
v4 = lambda: map(int, input().split())
v5 = True
v6 = 10 ** 9 + 7

def f1(a1):
    if v5:
        print(a1)

def f2(a1, a2):
    v1 = a1
    for v2 in range(1, a2):
        v1 = v1 * (a1 - v2) % v6
    return v1

def f3(a1, a2):
    v1 = len(dst[a2]) - 1
    if v1 == 0:
        return k - 1
    v2 = f2(k - 2, v1)
    for v3 in dst[a2]:
        if v3 == a1:
            continue
        v2 = v2 * f3(a2, v3) % v6
    return v2
sys.setrecursionlimit(250000)
v7, v8 = resource.getrlimit(resource.RLIMIT_STACK)
resource.setrlimit(resource.RLIMIT_STACK, (200000, v8))
v9, v10 = v4()
v11 = [[] for v12 in range(v9)]
for v12 in range(v9 - 1):
    v13, v14 = v4()
    v13 -= 1
    v14 -= 1
    v11[v13].append(v14)
    v11[v14].append(v13)
v15 = 1
for v12 in range(v9):
    v16 = len(v11[v12])
    v15 = v15 * f2(v10 - 1, v16) % v6
print(v15)
