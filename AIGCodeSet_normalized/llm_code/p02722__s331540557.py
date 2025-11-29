v1 = int(input())
v2 = 0

def f1(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    return v1
v3 = f1(v1 - 1)
v4 = f1(v1)
v2 += len(v3)
for v5 in v4:
    v6 = v5
    while v6 % K == 0:
        v6 = v6 // K
    if v6 % K == 1:
        v2 += 1
print(v2)
