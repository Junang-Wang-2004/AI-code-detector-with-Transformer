import sys
from bisect import bisect, bisect_left
import heapq

def f1():
    input = sys.stdin.readline
    v1, v2 = map(int, input().split())
    v3 = [int(a) for v4 in input().split()]
    v3.sort()
    v5 = [0] * (v1 + 1)
    for v6, v4 in enumerate(v3):
        v5[v6 + 1] = v4 + v5[v6]
    v7, v8 = (1, v3[v1 - 1] * 2 + 1)
    while v8 - v7 > 1:
        v9 = (v8 + v7) // 2
        v10 = 0
        for v6, v4 in enumerate(v3):
            v10 += v1 - bisect_left(v3, v9 - v4)
        if v10 >= v2:
            v7 = v9
        else:
            v8 = v9
    v11 = 0
    v10 = 0
    v12 = []
    heapq.heapify(v12)
    for v6, v4 in enumerate(v3):
        v13 = bisect_left(v3, v7 - v4)
        v11 += v4 * (v1 - v13) + (v5[v1 - 1] - v5[v13 - 1])
        v10 += v1 - v13
        for v14 in range(min(3, v1 - v13)):
            heapq.heappush(v12, v4 + v3[v13 + v14])
    if v10 > v2:
        for v15 in range(v10 - v2):
            v16 = heapq.heappop(v12)
            v11 -= v16
    print(v11)
    return 0
if __name__ == '__main__':
    f1()
