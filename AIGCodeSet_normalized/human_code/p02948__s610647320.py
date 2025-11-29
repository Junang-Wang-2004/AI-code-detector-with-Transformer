from heapq import heappop, heappush

def f1():
    v1, v2 = map(int, input().split())
    v3 = [tuple(map(int, input().split())) for v4 in range(v1)]
    v3.sort()
    v5 = 0
    v6 = 0
    v7 = []
    for v8 in range(1, v2 + 1):
        while v6 < v1 and v3[v6][0] <= v8:
            heappush(v7, -v3[v6][1])
            v6 += 1
        if v7:
            v5 -= heappop(v7)
    print(v5)
if __name__ == '__main__':
    f1()
