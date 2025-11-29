v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
v5 = [0] * v1
for v4 in range(v1 - 1):
    v6, v7 = map(int, input().split())
    v3[v6 - 1].append(v7 - 1)
    v3[v7 - 1].append(v6 - 1)

def f1(a1, a2, a3):
    v5[a1] += a3
    for v1 in v3[a1]:
        if v1 != a2:
            f1(v1, a1, a3)
for v4 in range(v2):
    v8, v9 = map(int, input().split())
    f1(v8 - 1, -1, v9)
print(*v5)
