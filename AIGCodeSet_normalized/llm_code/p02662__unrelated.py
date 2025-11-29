def f1(a1, a2, a3):
    v1 = 998244353
    v2 = [[0 for v3 in range(a2 + 1)] for v3 in range(a1 + 1)]
    v2[0][0] = 1
    for v4 in range(1, a1 + 1):
        v2[v4][0] = 1
        for v5 in range(1, a2 + 1):
            v2[v4][v5] = v2[v4 - 1][v5]
            if v5 >= a3[v4 - 1]:
                v2[v4][v5] = (v2[v4][v5] + v2[v4 - 1][v5 - a3[v4 - 1]]) % v1
    v6 = 0
    for v4 in range(1, a1 + 1):
        v6 = (v6 + v2[v4][a2]) % v1
    return v6
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
print(f1(v1, v2, v3))
