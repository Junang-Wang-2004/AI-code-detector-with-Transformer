import math

def f1(a1):
    v1 = []
    v2 = 2
    while v2 * v2 <= a1:
        if a1 % v2:
            v2 += 1
        else:
            a1 //= v2
            v1.append(v2)
    if a1 > 1:
        v1.append(a1)
    return v1
v1 = int(input())
v2 = int(math.ceil(math.sqrt(v1)))
v3 = v2 * v2 - v1
if v3 == 0:
    v4 = 0
    v5 = 0
else:
    v6 = f1(v3)
    v4 = 1
    v5 = 1
    for v7 in v6:
        v8 = v6.count(v7)
        while v8 >= 2:
            v4 *= v7
            v5 *= v7
            v8 -= 2
        if v8 > 0:
            if v4 < v5:
                v4 *= v7
            else:
                v5 *= v7
print('0 0 {} {} {} {}'.format(v2, v4, v5, v2))
