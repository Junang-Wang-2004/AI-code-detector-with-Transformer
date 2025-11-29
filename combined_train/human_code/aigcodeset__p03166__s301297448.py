def f1():
    import sys
    sys.setrecursionlimit(10 ** 7)
    v1, v2 = list(map(int, sys.stdin.readline().split()))
    v3 = [[] for v4 in range(v1)]
    for v5 in range(v2):
        v6, v7 = list(map(int, sys.stdin.readline().split()))
        v3[v6 - 1].append(v7 - 1)
    v8 = [0] * v1

    def dfs(a1):
        if v8[a1]:
            return v8[a1]
        v1 = 0
        if not v3[a1]:
            return 0
        for v2 in v3[a1]:
            v1 = max(v1, dfs(v2) + 1)
        v8[a1] = v1
        return v1
    v9 = 0
    for v10 in range(v1):
        v9 = max(v9, dfs(v10))
    return v9
print(f1())
