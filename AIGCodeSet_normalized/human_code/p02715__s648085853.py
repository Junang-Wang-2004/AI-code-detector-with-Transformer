v1 = 10 ** 9 + 7

def f1(a1, a2):
    v1 = 1
    while a2 > 0:
        if a2 & 1:
            v1 = v1 * a1 % v1
        a2 //= 2
        a1 = a1 * a1 % v1
    return v1

def f2(a1, a2):
    v1 = [0] * (a2 + 1)
    v2 = 0
    for v3 in range(a2, 0, -1):
        v1[v3] = f1(a2 // v3, a1) - sum((v1[y] for v4 in range(2 * v3, a2 + 1, v3)))
        v1[v3] %= v1
        v2 += v1[v3] * v3
    return v2 % v1
v2, v3 = map(int, input().split())
print(f2(v2, v3))
