v1, *v2 = map(int, open(0).read().split())
v3 = v4 = v5 = 0
for v6 in range(v1):
    while v5 < v1 and v4 & v2[v5] == 0:
        v4 += v2[v5]
        v5 += 1
    v4 -= v2[v6]
    v3 += v5 - v6
print(v3)
