import sys
import copy

def f1():
    v1, v2 = map(int, input().split())
    v3 = [list(map(lambda x: int(x) - 1, input().split())) for v4 in range(v2)]
    v5, v6 = map(lambda x: int(x) - 1, input().split())
    v7 = [[] for v4 in range(v1)]
    for v8 in v3:
        v7[v8[0]].append(v8[1])
    v9 = [-10000] * v1
    from collections import deque
    v10 = deque([v5])
    v9[v5] = 0
    v11 = set([v5])
    for v12 in range(v2):
        v13 = v10.popleft()
        v14 = deque([v13])
        for v12 in range(3):
            v15 = set()
            while len(v14) > 0:
                v16 = v14.pop()
                for v17 in v7[v16]:
                    v15.add(v17)
            v14 = v15.copy()
        for v18 in v14:
            if v9[v18] < 0 and v18 not in v11:
                v9[v18] = v9[v13] + 1
                v10.append(v18)
                v11.add(v18)
                if v18 == v6:
                    print(v9[v18])
                    sys.exit()
    print(-1)
if __name__ == '__main__':
    f1()
