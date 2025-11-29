v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = 10 ** 9 + 7

def f1(a1, a2, a3, a4):
    v1 = [[0 for v2 in range(a4 + 1)] for v2 in range(a3 + 1)]
    v1[0][0] = 1
    for v3 in range(a3 + 1):
        for v4 in range(a4 + 1):
            if v3 > 0:
                v1[v3][v4] = (v1[v3][v4] + v1[v3 - 1][v4]) % v5
            if v4 > 0:
                v1[v3][v4] = (v1[v3][v4] + v1[v3][v4 - 1]) % v5
            if v3 > 0 and v4 > 0 and (a1[v3 - 1] == a2[v4 - 1]):
                v1[v3][v4] = (v1[v3][v4] - v1[v3 - 1][v4 - 1] + v5) % v5
    return v1[a3][a4]
print(f1(v3, v4, v1, v2))
