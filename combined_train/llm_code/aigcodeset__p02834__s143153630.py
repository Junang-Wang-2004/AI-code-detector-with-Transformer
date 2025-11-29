v1, v2, v3 = map(int, input().split())
v4 = [[] for v5 in range(v1 + 1)]
v6 = [0 for v5 in range(v1 + 1)]
v7 = [0 for v5 in range(v1 + 1)]
for v5 in range(v1 - 1):
    v8, v9 = map(int, input().split())
    v4[v8].append(v9)
    v4[v9].append(v8)

def f1(a1, a2=-1):
    for v1 in v4[a1]:
        if v1 == a2:
            continue
        v6[v1] = v6[a1] + 1
        f1(v1, a1)

def f2(a1, a2=-1):
    for v1 in v4[a1]:
        if v1 == a2:
            continue
        v7[v1] = v7[a1] + 1
        f2(v1, a1)
f1(v2)
f2(v3)
v10 = 0
for v5 in range(1, v1 + 1):
    if v6[v5] >= v7[v5]:
        continue
    v11 = v6[v5]
    v12 = v7[v5] - v6[v5]
    v10 = max(v10, v12 - 1 + v11)
print(v10)
