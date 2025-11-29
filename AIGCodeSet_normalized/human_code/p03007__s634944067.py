v1 = int(input())
v2 = sorted(list(map(int, input().split())))
if v2[v1 - 1] < 0:
    v3 = 2 * v2[v1 - 1] - sum(v2)
    print(v3)
    v4, v5 = (v2[v1 - 1], v2[0])
    for v6 in range(v1 - 1):
        print(v4, v5)
        v4 = v4 - v5
        v5 = v2[v6 + 1]
elif v2[0] >= 0:
    v3 = sum(v2) - 2 * v2[0]
    print(v3)
    v4, v5 = (v2[0], v2[1])
    for v6 in range(v1 - 2):
        print(v4, v5)
        v4 = v4 - v5
        v5 = v2[v6 + 2]
    print(v5, v4)
else:
    v7 = 0
    v3 = 0
    for v6 in range(v1):
        if v2[v6] < 0:
            v3 -= v2[v6]
        else:
            if v2[v6 - 1] < 0 and v2[v6] >= 0:
                v7 = v6
            v3 += v2[v6]
    print(v3)
    v4 = v2[0]
    for v6 in range(v7, v1 - 1):
        print(v4, v2[v6])
        v4 -= v2[v6]
    v5 = v2[v1 - 1]
    print(v5, v4)
    v5 -= v4
    for v6 in range(1, v7):
        print(v5, v2[v6])
        v5 -= v2[v6]
