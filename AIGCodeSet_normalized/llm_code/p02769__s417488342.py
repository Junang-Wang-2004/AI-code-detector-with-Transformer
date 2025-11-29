v1, v2 = map(int, input().split())
v3 = pow(10, 9) + 7

def f1(a1, a2):
    v1 = 1
    v2 = 1
    for v3 in range(a2):
        v1 *= a1 - v3
        v1 %= v3
        v2 *= v3 + 1
        v2 %= v3
    return v1 * pow(v2, v3 - 2, v3) % v3
if v1 <= v2 - 1:
    print(f1(2 * v1 - 1, m))
else:
    v4 = 0
    for v5 in range(v2 + 1):
        v4 += f1(v1, v5) * f1(v1 - 1, a) % v3
print(v4 % v3)
