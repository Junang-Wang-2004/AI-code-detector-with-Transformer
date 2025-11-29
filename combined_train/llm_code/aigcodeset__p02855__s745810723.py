import numpy as np
v1, v2, v3 = map(int, input().split())
v4 = [list(input()) for v5 in range(v1)]
v6 = ((1, 0), (-1, 0), (0, 1), (0, -1))
v7 = [[0] * v2 for v5 in range(v1)]

def f1(a1, a2, a3):
    v7[a1][a2] = a3
    for v1, v2 in v6:
        v3 = a1 + v1
        v4 = a2 + v2
        if 0 <= v3 < v1 and 0 <= v4 < v2 and (v7[v3][v4] == 0) and (v4[v3][v4] == '.'):
            f1(v3, v4, a3)
v8 = 1
for v9 in range(v1):
    for v10 in range(v2):
        if v4[v9][v10] == '#':
            f1(v9, v10, v8)
            v8 += 1
for v9 in range(v1):
    if v7[v9][0] == 0:
        v7[v9][0] = v7[v9][1]
    for v10 in range(1, v2):
        if v7[v9][v10] == 0:
            v7[v9][v10] = v7[v9][v10 - 1]
for v9 in range(v1):
    for v10 in range(v2):
        print(v7[v9][v10], end=' ')
    print()
