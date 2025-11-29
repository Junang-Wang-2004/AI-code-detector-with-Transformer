import sys
sys.setrecursionlimit(10 ** 7)
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3.append((v5, v6))
v7 = [[10 ** 9] * (v1 + 1) for v4 in range(v2 + 1)]
for v8 in range(v2):
    v7[v8][0] = 0
for v8 in range(v2):
    for v9 in range(v1 + 1):
        if v9 < v3[v8][0]:
            v7[v8 + 1][v9] = v7[v8][v9]
        else:
            v7[v8 + 1][v9] = min(v7[v8][v9], v7[v8 + 1][v9 - v3[v8][0]] + v3[v8][1])
print(v7[v2][v1])
