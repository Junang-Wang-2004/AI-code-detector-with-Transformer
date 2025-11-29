import math
import copy

def f1(a1):
    v1 = [a1]
    for v2 in range(2, math.floor(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if a1 // v2 != v2:
                v1.append(a1 // v2)
    return v1
v1 = int(input())
v2 = f1(v1)
v3 = f1(v1 - 1)
v4 = 0
for v5 in v2:
    v6 = copy.deepcopy(v1)
    while v6 % v5 == 0:
        v6 = v6 // v5
    if v6 % v5 == 1:
        v4 += 1
v4 += len(v3)
if v1 > 2:
    print(v4)
else:
    print(1)
