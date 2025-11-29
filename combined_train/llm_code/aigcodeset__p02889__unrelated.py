import heapq
from collections import defaultdict

def f1(a1, a2, a3):
    v1 = {node: float('inf') for v2 in a1}
    v1[a2] = 0
    v3 = [(0, a2, 0)]
    while v3:
        v4, v2, v5 = heapq.heappop(v3)
        if v4 > v1[v2]:
            continue
        for v6, v7 in a1[v2].items():
            v8 = v4 + v7
            v9 = v5
            if v8 > a3:
                v8 = v7
                v9 += 1
            if v8 < v1[v6]:
                v1[v6] = v8
                heapq.heappush(v3, (v8, v6, v9))
    return v1

def f2():
    v1, v2, v3 = map(int, input().split())
    v4 = defaultdict(dict)
    for v5 in range(v2):
        v6, v7, v8 = map(int, input().split())
        v4[v6][v7] = v8
        v4[v7][v6] = v8
    v9 = int(input())
    for v5 in range(v9):
        v10, v11 = map(int, input().split())
        v12 = f1(v4, v10, v3)
        if v12[v11] == float('inf'):
            print(-1)
        else:
            print(v12[v11])
if __name__ == '__main__':
    f2()
