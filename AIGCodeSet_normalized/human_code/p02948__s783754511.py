import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from heapq import heappush, heappushpop
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v2 + 1)]
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v5 <= v2:
        v3[v2 - v5].append(v6)
v7 = []
for v8 in range(v2 + 1):
    for v9 in v3[v8]:
        if len(v7) < v8 + 1:
            heappush(v7, v9)
        else:
            heappushpop(v7, v9)
v10 = sum(v7)
print(v10)
