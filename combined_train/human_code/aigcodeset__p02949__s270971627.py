v1 = float('inf')

def f1(a1, a2, a3):
    v1 = [0] + [v1] * (a2 - 1)
    for v2 in range(a2):
        for v3, v4, v5 in a1:
            if v1[v3] == v1:
                continue
            if v1[v4] > v1[v3] + v5:
                if v2 == a2 - 1:
                    v1[v4] = -v1
                else:
                    v1[v4] = v1[v3] + v5
    for v2 in range(a2):
        for v3, v4, v5 in a1:
            if v1[v3] == v1:
                continue
            v1[v4] = min(v1[v4], v1[v3] + v5)
    return v1
v2, v3, v4 = map(int, input().split())
v5 = [None] * v3
for v6 in range(v3):
    v7, v8, v9 = map(int, input().split())
    v5[v6] = (v7 - 1, v8 - 1, -(v9 - v4))
v10 = f1(v5, v2, 0)
print(-1 if v10[v2 - 1] == -v1 else max(0, -v10[v2 - 1]))
