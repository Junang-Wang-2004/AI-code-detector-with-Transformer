v1 = int(input())
v2 = 2
for v3 in range(2, v1):
    if v3 * v3 > v1:
        break
    v4 = v1
    if v4 % v3 != 0:
        continue
    while v4 % v3 == 0:
        v4 //= v3
    if v4 % v3 == 1:
        v2 += 1
v5 = 0
v6 = v1 - 1
for v3 in range(2, v1):
    if v3 * v3 >= v6:
        break
    if v6 % v3 == 0:
        v5 += 2
if v3 * v3 == v6:
    v5 += 1
print(v2 + v5)
