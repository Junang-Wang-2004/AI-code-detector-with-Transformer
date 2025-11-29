v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4 = {}

def f1(a1, a2):
    if a1 == 1:
        return 1
    if a1 in v4:
        return v4[a1]
    v1 = pow(a1, a2, v3)
    for v2 in range(2, a1 + 1):
        v1 -= f1(a1 // v2, a2)
        v1 %= v3
    v4[a1] = v1
    return v1
print(sum((f1(v2 // i, v1) * i for v5 in range(1, v2 + 1))) % v3)
