v1 = int(input())
v2 = 0
for v3 in range(1, v1 + 1):
    v4 = 0
    if v3 % 2 != 0:
        for v5 in range(1, v3 + 1):
            if v3 % v5 == 0:
                v4 += 1
    if v4 == 8:
        v2 += 1
print(v2)
