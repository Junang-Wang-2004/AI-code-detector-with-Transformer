import sys
import collections
sys.setrecursionlimit(10 ** 6)

def f1(a1, a2):
    v1 = 0
    for v2 in a2[a1]:
        v1 = max(v1, f1(v2, a2) + 1)
    return v1

def f2():
    v1 = sys.stdin.buffer.readline
    v2 = 10 ** 9 + 7
    v3, v4 = list(map(int, v1().split()))
    v5 = collections.defaultdict(list)
    for v6 in range(v4):
        v7, v8 = list(map(int, v1().split()))
        v5[v7 - 1] += [v8 - 1]
    v9 = 0
    for v6 in range(v3):
        v9 = max(v9, f1(v6, v5))
    print(v9)
if __name__ == '__main__':
    f2()
