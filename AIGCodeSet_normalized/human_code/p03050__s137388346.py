import math
v1 = int(input())
v2 = v1 ** 0.5
if v2 - v2 // 1 != 0:
    v2 = int(v2 // 1)
else:
    v2 = int(v2 // 1) - 1
v3 = 0
for v4 in range(1, v2 + 1):
    if (v1 - v4) / v4 - (v1 - v4) // v4 == 0:
        if int((v1 - v4) // v4) != v4:
            v3 += int((v1 - v4) // v4)
print(v3)
