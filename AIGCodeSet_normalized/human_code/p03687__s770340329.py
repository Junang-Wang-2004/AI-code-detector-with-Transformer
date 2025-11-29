v1 = input().strip()
v2 = set(v1)
v3 = pow(100, 3)
for v4 in v2:
    v5 = v1
    v6 = 0
    while v5.count(v4) != len(v5):
        v7 = ''
        for v8, v9 in zip(v5, v5[1:]):
            if v8 == v4 or v9 == v4:
                v7 += v4
            else:
                v7 += v8
        v5 = v7
        v6 += 1
    if v3 > v6:
        v3 = v6
print(v3)
