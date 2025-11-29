import math
v1 = int(input())
if v1 == 2:
    print(1)
else:
    v2 = int(math.sqrt(v1) // 1)
    v3 = []
    for v4 in range(2, v2 + 1):
        if v1 % v4 == 0:
            v3.append(v4)
            if v4 * v4 != v1:
                v3.append(v1 // v4)
    v5 = 0
    for v4 in range(len(v3)):
        v6 = v1
        while v6 % v3[v4] == 0:
            v6 //= v3[v4]
        if v6 % v3[v4] == 1:
            v5 += 1
    if v1 % 2 == 1:
        v5 += 1
    print(v5)
