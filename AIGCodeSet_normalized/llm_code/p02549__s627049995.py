import math
v1 = 998244353
v2, v3 = list(map(int, input().split()))
v4 = [list(map(int, input().split())) for v5 in range(v3)]
v6 = [0] * (v2 + 1)
v7 = [0] * (v2 + 1)

def f1():
    v6[1] = 1
    v7[1] = 1
    for v1 in range(2, v2 + 1):
        for v2 in v4:
            if v1 - v2[0] >= 0:
                v6[v1] += v7[v1 - v2[0]]
            if v1 - v2[1] >= 0:
                v6[v1] -= v7[v1 - v2[1]]
        v6[v1] = v6[v1] % v1
        v7[v1] = (v7[v1 - 1] + v6[v1]) % v1
    print(v6[v2])
f1()
