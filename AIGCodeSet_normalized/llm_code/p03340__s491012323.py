v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = [0] * v1
v5 = 0
v6 = 0
for v3 in range(v1):
    v7 = 0
    for v8 in range(22):
        if v2[v3] & 1 << v8:
            if v4[v8]:
                v7 = 1
    if v7:
        v5 += v6 * (v6 + 1) // 2
        v4 = [0] * 22
        v6 = 1
        for v8 in range(22):
            if v2[v3] & 1 << v8:
                v4[v8] = 1
    else:
        v6 += 1
        for v8 in range(22):
            if v2[v3] & 1 << v8:
                v4[v8] = 1
v5 += v6 * (v6 + 1) // 2
print(v5)
