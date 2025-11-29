v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7

def f1(a1, a2, a3):
    v1 = 1
    for v2 in range(a2):
        v1 *= a1 - v2
        v1 *= pow(v2 + 1, a3 - 2, a3)
        v1 %= a3
    return v1
v4 = f1(2 * (v1 - 1) + v2, v1 - 1, v3)
v5 = f1(2 * (v1 - 1) + v2, v1, v3)
v6 = (v4 + v5) % v3
print(v6)
