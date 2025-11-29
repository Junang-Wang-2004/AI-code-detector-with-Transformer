import sys
input = sys.stdin.readline
from collections import defaultdict

def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = [[] for v5 in range(v1)]
    v6 = defaultdict(int)
    for v5 in range(v2):
        v7, v8, v9 = map(int, input().split())
        v7, v8 = (v7 - 1, v8 - 1)
        v6[v7, v8] = v9 - v3
        v4[v7].append(v8)
    v10 = 10 ** 14 * 2
    v11 = [v10] * v1
    v11[0] = 0
    for v5 in range(v1 - 1):
        for v12 in v6:
            v13, v14 = v12
            if v11[v13] + v6[v12] < v11[v14]:
                v11[v14] = v11[v13] + v6[v12]
    v15 = v11[v1 - 1]
    for v5 in range(v1 - 1):
        for v12 in v6:
            v13, v14 = v12
            if v11[v13] + v6[v12] < v11[v14]:
                v11[v14] = v11[v13] + v6[v12]
    if v11[v1 - 1] < v15:
        print(-1)
        return
    print(max(-v15, 0))
if __name__ == '__main__':
    f1()
