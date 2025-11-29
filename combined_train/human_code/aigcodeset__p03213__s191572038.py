import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
v1 = float('inf')

def f1():
    return int(input())

def f2():
    return float(input())

def f3():
    return input()

def f4():
    return [int(x) for v1 in input().split()]

def f5():
    return [int(x) - 1 for v1 in input().split()]

def f6():
    return [float(x) for v1 in input().split()]

def f7():
    return input().split()

def f8(a1):
    v1 = []
    v2 = a1
    while v2 % 2 == 0:
        v1.append(2)
        v2 //= 2
    for v3 in range(3, int(a1 ** 0.5) + 1, 2):
        while v2 % v3 == 0:
            v1.append(v3)
            v2 //= v3
    if v2 > 1:
        v1.append(v2)
    return collections.Counter(v1)

def f9():
    v1 = f1()
    v2 = collections.Counter()
    for v3 in range(1, v1 + 1):
        v4 = f8(v3)
        for v5, v6 in v4.items():
            v2[v5] += v6
    v7 = list(v2.values())
    v7.sort()
    v8 = len(v2)
    v9 = 0
    v10 = v8 - bisect.bisect_left(v7, 2)
    v11 = v8 - bisect.bisect_left(v7, 4)
    v12 = v8 - bisect.bisect_left(v7, 14)
    v13 = v8 - bisect.bisect_left(v7, 24)
    v14 = v8 - bisect.bisect_left(v7, 74)
    v9 += v11 * (v11 - 1) // 2 * max(v10 - 2, 0)
    v9 += v13 * max(v10 - 1, 0)
    v9 += v12 * max(v11 - 1, 0)
    v9 += v14
    print(v9)
if __name__ == '__main__':
    f9()
