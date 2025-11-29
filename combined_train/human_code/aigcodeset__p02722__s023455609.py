import math
v1 = int(input())
v2 = int(math.sqrt(v1 - 1))
v3 = []
for v4 in range(1, v2 + 1):
    if (v1 - 1) % v4 == 0:
        if v4 != 1:
            v3.append(v4)
        if (v1 - 1) // v4 != v4:
            v3.append((v1 - 1) // v4)
v5 = len(v3)
v6 = int(math.sqrt(v1))
v7 = []
for v4 in range(1, v6 + 1):
    if v1 % v4 == 0:
        if v4 != 1:
            v7.append(v4)
        if v1 // v4 != v4:
            v7.append(v1 // v4)
for v8 in v7:
    v9 = v1
    while v9 % v8 == 0:
        v9 //= v8
    if v9 % v8 == 1:
        v5 += 1
print(v5)
