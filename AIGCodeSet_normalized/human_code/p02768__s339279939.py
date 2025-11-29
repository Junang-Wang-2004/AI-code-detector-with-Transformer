def f1(a1, a2, a3):
    v1 = 1
    v2 = 1
    for v3 in range(min(a2, a1 - a2)):
        v1 = v1 * (a1 - v3) % a3
        v2 = v2 * (v3 + 1) % a3
    v2 = pow(v2, a3 - 2, a3)
    return v1 * v2 % a3
v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5 = f1(v1, v2, v4)
v6 = f1(v1, v3, v4)
v7 = pow(2, v1, v4) - 1 - v5 - v6
while v7 < 0:
    v7 += v4
print(v7)
