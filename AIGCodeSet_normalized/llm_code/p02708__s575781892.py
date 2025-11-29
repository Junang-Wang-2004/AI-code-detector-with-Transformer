v1, v2 = map(int, input().split())
v3 = 0
v4 = {}

def f1(a1, a2):
    if a2 == 0 or a2 == a1:
        return 1
    if a2 == 1:
        return a1
    if (a1, a2) in v4:
        return v4[a1, a2]
    v4[a1, a2] = f1(a1 - 1, a2) + f1(a1 - 1, a2 - 1)
    return v4[a1, a2]
if v1 <= v2:
    print(1)
else:
    for v5 in range(v2, v1 + 1):
        v3 += f1(v1 + 1, v5)
    print(v3)
