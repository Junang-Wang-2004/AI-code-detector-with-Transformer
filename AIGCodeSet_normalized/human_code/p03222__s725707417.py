import sys
v1 = sys.stdin.readline
v2 = 10 ** 9 + 7
v3, v4, v5 = map(int, v1().split())
v6 = [0] * max(v4 - 2 + 1, 3)
v6[1], v6[2] = (2, 3)
for v7 in range(3, len(v6)):
    v6[v7] = v6[v7 - 1] + v6[v7 - 2]
v8 = [[0 for v9 in range(v4)] for v7 in range(v3 + 1)]
v8[0][0] = 1

def f1(a1, a2):
    v1 = 1
    if 1 < a1:
        v1 *= v6[a1 - 1]
        v1 %= v2
    if v4 - 1 - (a2 + 1) >= 1:
        v1 *= v6[v4 - 1 - (a2 + 1)]
        v1 %= v2
    return v1
for v7 in range(v3):
    for v9 in range(v4):
        if v9 + 1 < v4:
            v8[v7 + 1][v9 + 1] += v8[v7][v9] * f1(v9, v9 + 1)
            v8[v7 + 1][v9 + 1] %= v2
        if v9 - 1 >= 0:
            v8[v7 + 1][v9 - 1] += v8[v7][v9] * f1(v9 - 1, v9)
            v8[v7 + 1][v9 - 1] %= v2
        v8[v7 + 1][v9] += v8[v7][v9] * f1(v9, v9)
        v8[v7 + 1][v9] % v2
print(v8[v3][v5 - 1] % v2)
