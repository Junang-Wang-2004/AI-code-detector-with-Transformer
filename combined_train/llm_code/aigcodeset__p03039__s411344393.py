v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7

def f1(a1, a2):
    v1 = 1
    if a1 < 2 * a2:
        a2 = a1 - a2
    for v3 in range(1, a2 + 1):
        v1 = v1 * (a1 - v3 + 1) / v3 % v4
    return v1
if v3 == 2:
    v5 = 0
else:
    v6 = 0
    v7 = 0
    for v8 in range(1, v1):
        v6 += v8 * (v1 - v8)
    for v8 in range(1, v2):
        v7 += v8 * (v2 - v8)
    v6 *= v2 ** 2
    v7 *= v1 ** 2
    v5 = f1(v1 * v2 - 2, v3 - 2) % v4
    v5 *= v6 + v7
print(int(v5 % v4))
