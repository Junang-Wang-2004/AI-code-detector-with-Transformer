import sys
from heapq import heapify, heappop, heappush
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
v4 = 10 ** 15

def f1(a1):
    v1 = [(v4, v4)] * (N + 1)
    v1[a1] = (0, L)
    v2 = 0
    v3 = L
    v4 = [(v2, v3, a1)]
    while v4:
        v5, v6, v7 = heappop(v4)
        if v1[v7][0] < v5:
            continue
        for next, v8 in graph[v7]:
            if v6 < v8:
                v9 = v5 + 1
                v10 = L - v8
            else:
                v9 = v5
                v10 = v6 - v8
            if v1[next][0] > v9 or (v1[next][0] == v9 and v1[next][1] > v10):
                v1[next] = (v9, v10)
                heappush(v4, (v9, v10, next))
    return v1
v5, v6, v7 = v3()
v8 = [[] for v9 in range(v5 + 1)]
for v9 in range(v6):
    v10, v11, v12 = v3()
    if v12 > v7:
        continue
    v8[v10].append((v11, v12))
    v8[v11].append((v10, v12))
v13 = v2()
for v9 in range(v13):
    v14, v15 = v3()
    v16 = f1(v14)
    print(-1 if v16[v15][0] == v4 else v16[v15][0])
