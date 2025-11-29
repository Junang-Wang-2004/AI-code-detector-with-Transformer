v1 = int(input())
v2 = [(int(input()), int(input())) for v3 in range(v1)]

def f1(a1, a2, a3, a4):
    return ((a1 - a3) ** 2 + (a2 - a4) ** 2) ** 0.5
v4 = [[] for v5 in range(v1)]
v4[0] = [str(v3) for v3 in range(v1)]
for v6 in range(v1 - 1):
    for v7 in range(v1):
        for v8 in v4[v6]:
            if not str(v7) in v8:
                v4[v6 + 1] += [v8 + str(v7)]
v9 = v4[-1]
v10 = sum((sum((f1(*v2[int(path[v3])], *v2[int(path[v3 + 1])]) for v3 in range(v1 - 1))) for v11 in v9)) / len(v9)
print(v10)
