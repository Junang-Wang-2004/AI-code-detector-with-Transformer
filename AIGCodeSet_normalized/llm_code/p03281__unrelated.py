def f1(a1):
    v1 = 0
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            if v2 == a1 // v2:
                v1 += 1
            else:
                v1 += 2
    return v1
v1 = int(input())
v2 = 0
for v3 in range(1, v1 + 1, 2):
    if f1(v3) == 8:
        v2 += 1
print(v2)
