import sys
from collections import defaultdict
v1 = sys.stdin.readline
v2 = sys.stdin.read

def f1():
    v1 = int(v1())
    v2 = [list(map(int, sys.stdin.readline().split())) for v3 in range(v1)]
    v4 = dict((((i, j), v2[i][j]) for v5 in range(v1) for v6 in range(v1)))
    v7 = defaultdict(int)
    v7.update(v4)
    for v8 in range(v1):
        for v5 in range(v1):
            for v6 in range(v1):
                v7[v5, v6] = min(v7[v5, v6], v7[v5, v8] + v7[v8, v6])
    v9 = [e for v10 in v4.keys() if v10[0] < v10[1]]
    v9.sort(key=v4.get, reverse=True)
    v11 = 0
    for v10 in v9:
        if v7[v10] < v4[v10]:
            print(-1)
            return None
        v12 = min([v7[v10[0], v5] + v7[v5, v10[1]] for v5 in range(v1) if v5 != v10[0] and v5 != v10[1]])
        if v12 >= v7[v10]:
            v11 += v4[v10]
    print(v11)
if __name__ == '__main__':
    f1()
