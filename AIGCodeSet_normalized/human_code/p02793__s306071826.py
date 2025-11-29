def f1():
    from fractions import gcd
    v1 = int(input())
    v2 = list(map(int, input().split()))

    def lcm(a1, a2):
        return a1 * a2 // gcd(a1, a2)
    v3 = 1
    v4 = 10 ** 9 + 7
    v5 = 0
    v6 = 1
    for v7 in v2:
        v6 = v6 * v7 // gcd(v6, v7)
    for v7 in v2:
        v5 += v6 // v7
    v5 %= v4
    print(v5)
f1()
