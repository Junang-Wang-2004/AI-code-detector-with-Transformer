import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
v5 = [0] * v1
for v4 in range(v1 - 1):
    v6, v7 = map(int, input().split())
    v3[v6 - 1].append(v7 - 1)
    v3[v7 - 1].append(v6 - 1)
for v4 in range(v2):
    v8, v9 = map(int, input().split())
    v5[v8 - 1] += v9
sys.setrecursionlimit(10 ** 6)

def f1(a1, a2):
    v1 = v3[a1]
    for v2 in v1:
        if v2 == a2:
            continue
        v5[v2] += v5[a1]
        f1(v2, a1)
f1(0, -1)
print(' '.join(map(str, v5)))
