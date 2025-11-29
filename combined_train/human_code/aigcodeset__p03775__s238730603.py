v1 = int(input())
if v1 == 1:
    print(1)
    exit()

def f1(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    return v1
v2 = f1(v1)
v2.sort()
v3 = 100
for v4 in v2:
    if v4 > v1 // 2:
        break
    v5 = v1 // v4
    v3 = min(max(len(str(v4)), len(str(v5))), v3)
print(v3)
