import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = [{} for v4 in range(v1)]
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v3[v6 - 1][v7 - 1] = 1
v8 = {}

def f1(a1):
    v1 = 0
    if a1 in v8:
        return v8[a1]
    else:
        for v2 in v3[a1]:
            if v2 in v8:
                v1 = max(v8[v2] + 1, v1)
            else:
                v1 = max(f1(v2) + 1, v1)
        v8[a1] = v1
        return v1
v9 = 0
for v5 in range(v1):
    v9 = max(v9, f1(v5))
print(v9)
