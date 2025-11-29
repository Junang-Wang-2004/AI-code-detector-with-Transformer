def f1(a1, a2):
    v1 = 0
    for v2 in range(1, a1 + 1):
        for v3 in range(a1 - v2 + 1):
            v4 = v3 + v2
            v5 = a2[v3]
            v6 = a2[v3]
            for v7 in range(v3 + 1, v4):
                v5 ^= a2[v7]
                v6 += a2[v7]
            if v5 == v6:
                v1 += 1
    return v1
v1 = int(input())
v2 = list(map(int, input().split()))
print(f1(v1, v2))
