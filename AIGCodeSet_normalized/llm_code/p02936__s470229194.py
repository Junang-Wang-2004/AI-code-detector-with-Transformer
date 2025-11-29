import sys
sys.setrecursionlimit(10 ** 7)
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1 - 1)]
v5 = [list(map(int, input().split())) for v4 in range(v2)]
v6 = [[] for v4 in range(v1 + 3)]
for v7, v8 in v3:
    v6[v7].append(v8)
    v6[v8].append(v7)
v9 = [0] * (v1 + 1)
for v10, v11 in v5:
    v9[v10] += v11

def f1(a1, a2):
    v9[a1] += a2
    for v1 in v6[a1]:
        f1(v1, a2)
f1(1, 0)
print(*v9[1:], end='\t')
