import sys
sys.setrecursionlimit(10000000)
v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v5 = [[0] * v2 for v4 in range(v1)]

def f1(a1, a2, a3):
    if v3[a1][a2] == '.':
        v1 = [1, 0]
    else:
        v1 = [0, 1]
    v2 = [-1, 1, 0, 0]
    v3 = [0, 0, -1, 1]
    a3[a1][a2] = 1
    for v4 in range(4):
        v5 = a1 + v2[v4]
        v6 = a2 + v3[v4]
        if 0 <= v5 <= v1 - 1 and 0 <= v6 <= v2 - 1:
            if a3[v5][v6] == 0 and v3[v5][v6] != v3[a1][a2]:
                v7, v8 = f1(v5, v6, a3)
                v1[0] += v7
                v1[1] += v8
    return v1
v6 = 0
for v7 in range(v1):
    for v8 in range(v2):
        if v5[v7][v8] != 1:
            v9, v10 = f1(v7, v8, v5)
            v6 += v9 * v10
print(v6)
