import sys
v1, v2 = map(int, input().split())
v3 = 998244353
v4 = [0] * (v1 + 1)
v4[1] = 1
v5 = [tuple(map(int, input().split())) for v6 in range(v2)]
v7 = [0 for v6 in range(v2)]
for v8 in range(2, v1 + 1):
    v9 = 0
    for v10 in range(v2):
        v7[v10] += v4[max(0, v8 - v5[v10][0])] - v4[max(0, v8 - v5[v10][1] - 1)]
        v7[v10] %= v3
        v9 = (v9 + v7[v10]) % v3
    v4[v8] = v9
print(v4[v1])
