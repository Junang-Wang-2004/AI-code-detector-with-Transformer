from sys import stdin
from collections import deque

def f1():
    v1 = stdin.readline
    v2 = int(v1())
    v3 = v2 * (v2 - 1) // 2
    v4 = [list(map(lambda x: int(x) - 1, v1().split())) for v5 in range(v2)]
    v6 = dict()
    v7 = 0
    for v8 in range(v2 - 1):
        for v9 in range(v8 + 1, v2):
            v6[v8, v9] = v7
            v6[v9, v8] = v7
            v7 += 1
    v10 = [[] for v5 in range(v3)]
    v11 = [set() for v5 in range(v3)]
    for v8 in range(v2):
        for v9 in range(v2 - 1 - 1):
            v12 = v6[v8, v4[v8][v9]]
            v13 = v6[v8, v4[v8][v9 + 1]]
            v10[v12].append(v13)
            v11[v13].add(v12)
    v14 = []
    for v8 in range(v3):
        if len(v11[v8]) == 0:
            v14.append(v8)
    if len(v14) == 0:
        print(-1)
    else:
        v15 = []
        v16 = deque(v14)
        while len(v16) > 0:
            v14 = v16.popleft()
            v15.append(v14)
            v17 = v10[v14]
            for v8 in v17:
                v11[v8].remove(v14)
                if len(v11[v8]) == 0:
                    v16.append(v8)
        if len(v15) != v3:
            print(-1)
        else:
            v18 = [0] * v3
            v18[v15[0]] = 1
            for v8 in v15:
                for v9 in v10[v8]:
                    v18[v9] = max(v18[v9], v18[v8] + 1)
            print(max(v18))
if __name__ == '__main__':
    f1()
