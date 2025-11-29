v1 = int(input())
v2 = 0
for v3 in range(9, v1 + 1, 2):
    v4 = 2
    for v5 in range(2, int(v3 ** 0.5) + 1):
        if v3 % v5 == 0:
            if v3 // v5 == v5:
                v4 += 1
            else:
                v4 += 2
        if v4 > 8:
            break
    if v4 == 8:
        v2 += 1
print(v2)
