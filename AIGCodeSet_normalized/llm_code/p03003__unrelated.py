def f1(a1, a2):
    v1 = len(a1)
    v2 = len(a2)
    v3 = 10 ** 9 + 7
    v4 = [[0 for v5 in range(v2 + 1)] for v5 in range(v1 + 1)]
    for v6 in range(v1 + 1):
        v4[v6][0] = 1
    for v7 in range(v2 + 1):
        v4[0][v7] = 1
    for v6 in range(1, v1 + 1):
        for v7 in range(1, v2 + 1):
            v4[v6][v7] = (v4[v6 - 1][v7] + v4[v6][v7 - 1] - v4[v6 - 1][v7 - 1] + v3) % v3
            if a1[v6 - 1] == a2[v7 - 1]:
                v4[v6][v7] = (v4[v6][v7] + v4[v6 - 1][v7 - 1]) % v3
    return v4[v1][v2]
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
print(f1(v3, v4))
