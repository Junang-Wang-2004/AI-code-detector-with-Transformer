v1 = 10 ** 30

def f1(a1, a2, a3):
    v1 = [v1] * a2
    v2 = [False] * a2
    v1[a1] = 0
    for v3 in range(a2 - 1):
        for v4, v5, v6 in a3:
            if v1[v5] > v1[v4] + v6 and v1[v4] != v1:
                v1[v5] = min(v1[v5], v1[v4] + v6)
    for v3 in range(a2):
        for v4, v5, v6 in a3:
            if v1[v5] > v1[v4] + v6 and v1[v4] != v1:
                v1[v5] = v1[v4] + v6
                v2[v5] = True
            if v2[v4]:
                v2[v5] = True
    return (v1, v2)
v2, v3, v4 = map(int, input().split())
v5 = []
for v6 in range(v3):
    v7, v8, v9 = map(int, input().split())
    v5.append((v7 - 1, v8 - 1, -(v9 - v4)))
v10, v11 = f1(0, v2, v5)
if v11[v2 - 1]:
    print(-1)
else:
    v12 = -v10[v2 - 1]
    print(max(0, v12))
