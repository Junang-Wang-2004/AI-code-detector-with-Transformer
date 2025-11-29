from collections import Counter, defaultdict, deque
from bisect import bisect_left
import sys, math, itertools, pprint, fractions, time
sys.setrecursionlimit(10 ** 8)
v1 = 10 ** 9 + 7
v2 = float('inf')

def f1():
    return int(sys.stdin.readline())

def f2():
    return list(map(int, sys.stdin.readline().split()))
v3 = time.time()
v4 = f1()
v5 = []
for v6 in range(v4):
    v7 = f2()
    v5.append(deque(v7))
v8 = v4 * (v4 - 1) // 2
v9 = 0
while True:
    v9 += 1
    v10 = v8
    v11 = set()
    for v6 in range(v4):
        if v6 in v11 or v5[v6] == deque([]):
            continue
        v12 = True
        v13 = v5[v6][0] - 1
        if not v13 in v11 and v5[v13][0] == v6 + 1:
            v8 -= 1
            if not v8:
                print(v9)
                quit()
            v5[v6].popleft()
            v5[v13].popleft()
            v11.add(v6)
            v11.add(v13)
        v14 = time.time()
    if v10 == v8:
        print(-1)
        quit()
    if v14 - v3 > 1.7:
        print(v4 * (v4 - 1) // 2)
        quit()
