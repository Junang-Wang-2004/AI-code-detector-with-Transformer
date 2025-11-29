v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1 + 1)]
v5 = [-1 for v4 in range(v1 + 1)]
for v4 in range(v2):
    v6, v7 = map(int, input().split())
    v3[v6].append(v7)

def f1(a1):
    if v5[a1] != -1:
        return v5[a1]
    else:
        v1 = 0
        for v2 in v3[a1]:
            v1 = max(v1, f1(v2) + 1)
        v5[a1] = v1
        return v1
v8 = 0
for v9 in range(1, v1 + 1):
    v8 = max(v8, f1(v9))
print(v8)
