def f1(a1):
    v1, v2 = ([], [])
    v3 = 1
    while v3 * v3 <= a1:
        if a1 % v3 == 0:
            v1.append(v3)
            if v3 != a1 // v3:
                v2.append(a1 // v3)
        v3 += 1
    return v1 + v2[::-1]
v1 = int(input())
v2 = v1 - 1
v3 = len(f1(v2)) - 1
v4 = f1(v1)
for v5 in v4:
    if v5 == 1:
        continue
    v6 = v1
    while True:
        if v6 % v5 == 0:
            v6 = v6 // v5
        else:
            if v6 % v5 == 1:
                v3 += 1
            break
print(v3)
