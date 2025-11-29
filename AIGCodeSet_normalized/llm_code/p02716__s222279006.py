import sys
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: list(map(int, v1().split()))
from bisect import bisect_left, insort_left

def f1():
    v1 = v2()
    v2 = v3()
    v3 = [i for v4 in range(v1)]
    v2 = list(zip(v3, v2))
    v2.sort(key=lambda x: x[1], reverse=True)
    v5 = 0
    v6 = 0
    v7 = [-100]
    v8 = v1 // 2
    v4 = 0
    while v6 < v8:
        v9 = v2[v4][0]
        v10 = bisect_left(v7, v9)
        if v10 != 0:
            v11 = v7[v10 - 1]
        else:
            v11 = -10
        if v10 != len(v7):
            v12 = v7[v10]
        else:
            v12 = v7[v10 - 1]
        if v11 == v9 - 1 or v11 == v9 + 1 or v12 == v9 - 1 or (v12 == v9 + 1):
            v4 += 1
            continue
        v5 += v2[v4][1]
        insort_left(v7, v9)
        v6 += 1
        v4 += 1
    print(v5)
if __name__ == '__main__':
    f1()
