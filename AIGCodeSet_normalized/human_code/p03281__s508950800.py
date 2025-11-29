v1 = 0

def f1(a1):
    v1 = 0
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1 += 2 if v2 != a1 // v2 else 1
    return v1
for v2 in range(1, int(input()) + 1, 2):
    if f1(v2) == 8:
        v1 += 1
print(v1)
