import sys
sys.setrecursionlimit(1000000)

def f1(a1):
    if dp[a1] != -1:
        return dp[a1]
    for v1 in d[a1]:
        if dp[v1] != -1:
            dp[a1] = max(dp[a1], dp[v1] + 1)
        else:
            dp[a1] = max(dp[a1], f1(v1) + 1)
    return max(dp[a1], 0)
from collections import defaultdict as dd
v1, v2 = map(int, input().split())
v3 = dd(list)
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5].append(v6)
v7 = dd(lambda: -1)
v8 = 0
for v4 in range(1, v1 + 1):
    if v7[v4] == -1:
        v7[v4] = f1(v4)
    v8 = max(v8, v7[v4])
print(v8)
