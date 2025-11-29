v1 = int(input().strip())
v2 = 0
for v3 in range(1, v1 + 1, 2):
    v4 = 0
    for v5 in range(1, v3 + 1):
        if v5 * v5 > v3:
            break
        if v3 % v5 == 0:
            v4 += 2
            if v4 >= 9:
                break
    if v4 == 8:
        v2 += 1
print(v2)
