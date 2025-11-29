import sys
sys.setrecursionlimit(10000000)
v1 = 10 ** 9 + 7
v2 = 10 ** 15
from collections import deque, defaultdict, Counter

def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = [tuple(map(int, input().split())) for v5 in range(v3)]
    v6 = [0] * 10
    v7 = defaultdict(int)
    for v8, v9 in v4:
        for v10 in (-1, 0, 1):
            for v11 in (-1, 0, 1):
                if v8 + v10 <= 1 or v8 + v10 >= v1:
                    continue
                if v9 + v11 <= 1 or v9 + v11 >= v2:
                    continue
                v12 = (v8 + v10, v9 + v11)
                v6[v7[v12]] -= 1
                v7[v12] += 1
                v6[v7[v12]] += 1
    v6[0] += (v1 - 2) * (v2 - 2)
    print('\n'.join(map(str, v6)))
if __name__ == '__main__':
    f1()
