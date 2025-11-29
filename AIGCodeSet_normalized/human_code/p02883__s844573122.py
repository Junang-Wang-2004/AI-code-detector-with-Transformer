import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
v1 = []
v2 = []
v3 = 0

def f1(a1, a2, a3):
    if a1 + 1 < a2:
        v1 = (a1 + a2) // 2
        v2 = 0
        for v3 in range(v3):
            v2 += max(v1[v3] - v1 // v2[v3], 0)
        if v2 <= a3:
            return f1(a1, v1, a3)
        else:
            return f1(v1, a2, a3)
    else:
        return a2

def f2():
    global a, f, n
    v1, v2 = map(int, input().strip().split())
    v3 = list(map(int, input().strip().split()))
    v4 = list(map(int, input().strip().split()))
    v3 = sorted(v3)
    v4 = sorted(v4, reverse=True)
    print(f1(-1, 10 ** 12, v2))
if __name__ == '__main__':
    f2()
