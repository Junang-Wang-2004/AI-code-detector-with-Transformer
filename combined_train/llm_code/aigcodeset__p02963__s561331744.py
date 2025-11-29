v1 = int(input())
v2 = 2
v3 = True
v4 = 1
v5 = 1
while v2 * v2 <= v1:
    while v1 % v2 == 0:
        v1 /= v2
        if v3:
            v4 *= v2
        else:
            v5 *= v2
        v3 = not v3
    v2 += 1
if v1 > 1:
    if v3:
        v4 *= v1
    else:
        v5 *= v1
if v4 == 1 and v5 == 1:
    v5 = v1
print('0 0 {} 0 0 {}'.format(int(v4), int(v5)))
