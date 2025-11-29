def f1():
    v1 = 0
    v2 = int(input())
    v3 = [list(map(lambda x: int(x) - 1, input().split()))[::-1] for v4 in range(v2)]
    v5 = [0] * v2
    v6 = 0
    v7 = 0
    v8 = 0
    while v6 < v2 * (v2 - 1) // 2:
        while not v3[v7]:
            v7 = (v7 + 1) % v2
        v9 = v3[v7][-1]
        if not v3[v9]:
            return -1
        if v3[v9][-1] == v7:
            v5[v7] = max(v5[v7], v5[v9]) + 1
            v5[v9] = v5[v7]
            v3[v9].pop(-1)
            v3[v7].pop(-1)
            v6 += 1
            v8 = 0
        else:
            v7 = v9
            v8 += 1
        if v8 == v2:
            return -1
    v1 = max(v5)
    return v1
print(f1())
