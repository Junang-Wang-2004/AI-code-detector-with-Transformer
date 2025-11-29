import sys
from collections import defaultdict

def f1():
    v1, v2, v3 = map(int, sys.stdin.readline().split())
    v4 = defaultdict(list)
    for v5 in range(v1 - 1):
        v6, v7 = map(int, sys.stdin.readline().split())
        v4[v6].append(v7)
        v4[v7].append(v6)

    def dfs(a1, a2, a3):
        nonlocal max_depth, max_node
        if a3 > max_depth:
            v1 = a3
            v2 = a1
        for v3 in v4[a1]:
            if v3 != a2:
                dfs(v3, a1, a3 + 1)
    v8 = 0
    v9 = 0
    dfs(v2, -1, 0)
    v10 = v8
    v8 = 0
    v9 = 0
    dfs(v3, -1, 0)
    v11 = v8
    v12 = v9
    v8 = 0
    v9 = 0
    dfs(v12, -1, 0)
    v13 = v8
    v14 = v10 - v13
    v15 = v11 - v13
    v16 = v14 + v15
    print(v16)
f1()
