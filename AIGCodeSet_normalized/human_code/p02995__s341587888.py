from fractions import gcd
v1, v2, v3, v4 = map(int, input().split())
v1 -= 1

def f1(a1, a2):
    return a1 * a2 // gcd(a1, a2)
v5 = f1(v3, v4)
v6 = v1 // v5
v7 = v2 // v5
v8 = v1 // v3 + v1 // v4 - v6
v9 = v2 // v3 + v2 // v4 - v7
print(v2 - v1 - (v9 - v8))
