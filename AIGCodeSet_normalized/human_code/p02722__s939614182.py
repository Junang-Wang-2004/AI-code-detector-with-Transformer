v1 = int(input())

def f1(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    return v1
v2 = len(f1(v1 - 1)) - 1
v3 = f1(v1)
del v3[0]
for v4 in v3:
    v5 = v1
    while v5 % v4 == 0 and v5 != 0:
        v5 = v5 // v4
    if v5 % v4 == 1:
        v2 += 1
print(v2)
