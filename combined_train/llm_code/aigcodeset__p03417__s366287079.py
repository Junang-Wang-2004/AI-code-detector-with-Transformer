def f1(a1):
    if a1:
        return False
    else:
        return True
v1, v2 = map(int, input().split())
v3 = [[True for v4 in range(v2)] for v5 in range(v1)]
for v4 in range(v1):
    for v5 in range(v2):
        v3[v4][v5] = f1(v3[v4][v5])
        if v5 - 1 >= 0:
            v3[v4][v5 - 1] = f1(v3[v4][v5 - 1])
        if v5 + 1 < v2:
            v3[v4][v5 + 1] = f1(v3[v4][v5 + 1])
        if v4 - 1 >= 0:
            v3[v4 - 1][v5] = f1(v3[v4 - 1][v5])
            if v5 - 1 >= 0:
                v3[v4 - 1][v5 - 1] = f1(v3[v4 - 1][v5 - 1])
            if v5 + 1 < v2:
                v3[v4 - 1][v5 + 1] = f1(v3[v4 - 1][v5 + 1])
        if v4 + 1 < v1:
            v3[v4 + 1][v5] = f1(v3[v4 + 1][v5])
            if v5 - 1 >= 0:
                v3[v4 + 1][v5 - 1] = f1(v3[v4 + 1][v5 - 1])
            if v5 + 1 < v2:
                v3[v4 + 1][v5 + 1] = f1(v3[v4 + 1][v5 + 1])
print(sum([v4.count(False) for v4 in v3]))
