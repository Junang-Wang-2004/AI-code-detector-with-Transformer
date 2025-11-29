def f1(a1, a2, a3):
    v1 = 998244353
    v2 = [0] * (a1 + 1)
    v2[1] = 1
    v3 = set()
    for v4, v5 in a3:
        for v6 in range(v4, v5 + 1):
            v3.add(v6)
    for v6 in range(2, a1 + 1):
        for v7 in v3:
            if v6 - v7 >= 1:
                v2[v6] = (v2[v6] + v2[v6 - v7]) % v1
    return v2[a1]
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
print(f1(v1, v2, v3))
