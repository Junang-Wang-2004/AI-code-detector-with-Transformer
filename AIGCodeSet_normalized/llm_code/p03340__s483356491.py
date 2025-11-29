v1, *v2 = map(int, open('0').read().split())
v3 = 0
v4 = 0
v5 = v2[v3]
v6 = v2[v3]
v7 = 0
for v3 in range(v1):
    while v4 < v1 and v5 == v6:
        v4 += 1
        if v4 < v1:
            v5 += v2[v4]
            v6 ^= v2[v4]
    v7 += v4 - v3
    if v3 < v1 - 1:
        v5 -= v2[v3]
        v6 ^= v2[v3]
print(v7)
