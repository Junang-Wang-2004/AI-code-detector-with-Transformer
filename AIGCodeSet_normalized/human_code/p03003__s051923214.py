import sys
input = sys.stdin.readline
v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = [[1] * (v3 + 1) for v7 in range(v2 + 1)]
for v7 in range(v2):
    for v8 in range(v3):
        if v4[v7] == v5[v8]:
            v6[v7 + 1][v8 + 1] = v6[v7 + 1][v8] + v6[v7][v8 + 1]
        else:
            v6[v7 + 1][v8 + 1] = v6[v7 + 1][v8] + v6[v7][v8 + 1] - v6[v7][v8]
        v6[v7 + 1][v8 + 1] %= v1
print(v6[v2][v3])
