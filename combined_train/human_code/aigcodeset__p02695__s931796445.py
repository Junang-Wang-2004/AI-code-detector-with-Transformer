import sys
input = sys.stdin.readline
v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v3)]
v6 = []

def f1(a1, a2):
    if len(a2) == v1:
        v6.append(a2)
        return
    for v1 in range(a1, v2 + 1):
        f1(v1, a2 + [v1])
f1(1, [])
v7 = 0
for v8 in v6:
    v9 = 0
    for v10, v11, v12, v13 in v4:
        if v8[v11 - 1] - v8[v10 - 1] == v12:
            v9 += v13
    v7 = max(v7, v9)
print(v7)
