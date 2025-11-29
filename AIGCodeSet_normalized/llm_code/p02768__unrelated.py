def f1(a1, a2, a3):
    v1 = 1
    while a2 > 0:
        if a2 % 2 == 1:
            v1 = v1 * a1 % a3
        a1 = a1 * a1 % a3
        a2 //= 2
    return v1
v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = f1(2, v1, v4) - 1
v5 %= v4
if v2 <= v1:
    v5 -= f1(2, v1 - v2, v4)
    v5 %= v4
if v3 <= v1:
    v5 -= f1(2, v1 - v3, v4)
    v5 %= v4
v5 += v4
v5 %= v4
print(v5)
