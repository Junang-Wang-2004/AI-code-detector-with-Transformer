v1 = 0
v2 = 0
v3 = 0
while v2 < K:
    if v3 < 10:
        v2 += 1
    else:
        v4 = list(map(int, str(v3)))
        v5 = True
        for v6 in range(1, len(v4)):
            if abs(v4[v6] - v4[v6 - 1]) > 1:
                v5 = False
                break
        if v5:
            v2 += 1
            v1 = v3
    v3 += 1
print(v1)
