v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = []
for v5 in range(v2):
    v4.append(tuple(map(int, input().split())))
v6 = [[] for v5 in range(v1 + 1)]
for v7 in v4:
    v8, v9 = v7
    v6[v8].append(v9)
    v6[v9].append(v8)
v10 = [False] * (v1 + 1)

def f1(a1):
    v10[a1] = True
    group[-1].append(a1)
    for v1 in v6[a1]:
        if v10[v1] == False:
            f1(v1)
v11 = []
for v12 in range(1, v1 + 1):
    if v10[v12] == False:
        v11.append([])
        f1(v12)
v13 = 0
for v7 in v11:
    v14 = set(v7) & set([v3[v12 - 1] for v12 in v7])
    v13 += len(v14)
print(v13)
