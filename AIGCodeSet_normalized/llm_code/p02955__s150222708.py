from math import ceil, floor

def f1():
    v1 = input()
    v2 = 0
    v3 = []
    while v2 < len(v1):
        v4 = 0
        while v2 < len(v1) and v1[v2] == 'R':
            v4 += 1
            v2 += 1
        v5 = 0
        while v2 < len(v1) and v1[v2] == 'L':
            v5 += 1
            v2 += 1
        v6 = ceil(v4 / 2) + v5 // 2
        v7 = v4 // 2 + ceil(v5 / 2)
        v3.extend([0] * (v4 - 1))
        v3.append(v6)
        v3.append(v7)
        v3.extend([0] * (v5 - 1))
    print(*v3)
from heapq import heappush, heappop

def f2(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            heappush(v1, -v2)
            if v2 != a1 // v2:
                heappush(v1, -(a1 // v2))
    return v1

def f3():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = sum(v3)
    v5 = f2(v4)
    v6 = len(v5)
    for v7 in range(v6):
        v8 = -heappop(v5)
        v9 = []
        for v10 in v3:
            v9.append(v10 % v8)
        v11 = sum(v9)
        if v11 <= v2 * 2 and v11 % v8 == 0:
            print(v8)
            exit()
    print(0)
if __name__ == '__main__':
    f3()
