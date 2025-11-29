import sys
input = sys.stdin.readline
v1, v2 = (lambda: int(input()), lambda: [int(w) for v3 in input().split()])
import sys
sys.setrecursionlimit(10 ** 6)

def f1(a1):
    global grpah, vis, dp
    vis[a1] = 1
    for v1 in graph[a1]:
        if not vis[v1]:
            f1(v1)
        dp[a1] = max(dp[a1], dp[v1] + 1)
v4, v5 = v2()
v6 = {i: [] for v7 in range(1, v4 + 1)}
for v7 in range(v5):
    v8, v9 = v2()
    v6[v8].append(v9)
v10 = [0] * (v4 + 1)
v11 = [0] * (v4 + 1)
for v7 in range(1, v4 + 1):
    if not v11[v7]:
        f1(v7)
print(max(v10))
