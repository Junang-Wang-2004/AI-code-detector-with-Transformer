from math import ceil
import sys
sys.setrecursionlimit(10 ** 7)

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = list(map(int, input().split()))
    v3.sort()
    v4.sort(reverse=True)
    v5 = [(ae, fe) for v6, v7 in zip(v3, v4)]

    def bs(a1, a2, a3):
        if a1 == a2:
            return a2
        v1 = 0
        for v2, v3 in v5:
            v4 = max(0, ceil((v2 * v3 - a2) / v3))
            v1 += v4
        if v1 <= v2:
            return bs(a1, (a2 - a1) // 2 + a1, a2)
        else:
            return bs(a2 + 1, (a3 - a2 - 1) // 2 + a2 + 1, a3)
    v8 = bs(0, 10 ** 12 // 2, 10 ** 12)
    print(v8)
if __name__ == '__main__':
    f1()
