def f1():
    import sys
    input = sys.stdin.readline
    v1, v2, v3 = [int(i) for v4 in input().split()]
    v5 = []
    for v4 in range(v1):
        v6, v7 = [int(v4) for v4 in input().split()]
        v5.append((v6, 0, v7))
    from heapq import heapify, heappop, heappush
    heapify(v5)
    v8 = 0
    v9 = 0
    while v5:
        v6, v10, v7 = heappop(v5)
        if v10 == 0:
            if v8 * v3 >= v7:
                continue
            v11 = v7 - v8 * v3
            v12 = (v11 - 1) // v3 + 1
            heappush(v5, (v6 + 2 * v2, 1, v12))
            v9 += v12
            v8 += v12
        else:
            v8 -= v7
    print(v9)
if __name__ == '__main__':
    f1()
