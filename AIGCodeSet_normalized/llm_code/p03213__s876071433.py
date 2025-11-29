v1 = int(input())
v2 = list()
for v3 in range(1, v1 + 1):
    v4 = 2
    while v4 * v4 <= v3:
        while v3 % v4 == 0:
            v3 //= v4
            v2.append(v4)
        v4 += 1
    if v3 > 1:
        v2.append(v3)
v5 = v6 = 0
for v3 in range(2, v1 + 1):
    v7 = v2.count(v3)
    if v7 >= 2:
        v5 += 1
    if v7 >= 4:
        v6 += 1
print(v6 * (v6 - 1) // 2 * (v5 - 2))
