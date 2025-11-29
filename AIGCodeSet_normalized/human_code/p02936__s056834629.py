import sys
sys.setrecursionlimit(10000000)
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v4 in range(v1 - 1):
    v5, v6 = map(int, input().split())
    v3[v5 - 1].append(v6 - 1)
    v3[v6 - 1].append(v5 - 1)
v7 = [0] * v1
for v4 in range(v2):
    v8, v9 = map(int, input().split())
    v7[v8 - 1] += v9
v10 = set()

def f1(a1):
    v10.add(a1)
    for v1 in v3[a1]:
        if v1 not in v10:
            v7[v1] += v7[a1]
            f1(v1)
f1(0)
for v8 in v7:
    print(v8, end=' ')
