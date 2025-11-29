import sys
sys.setrecursionlimit(10000)
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5 - 1].append(v6 - 1)
print(v3)
v7 = [-1 for v4 in range(v1)]

def f1(a1):
    if v7[a1] != -1:
        return v7[a1]
    v1 = 0
    for v2 in v3[a1]:
        v1 = max(v1, f1(v2) + 1)
    v7[a1] = v1
    return v1
v8 = 0
for v9 in range(v1):
    v8 = max(v8, f1(v9))
print(v8)
