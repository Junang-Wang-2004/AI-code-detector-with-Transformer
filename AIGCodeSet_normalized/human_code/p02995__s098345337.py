import math

def f1(a1, a2):
    return a1 * a2 // math.gcd(a1, a2)
v1, v2, v3, v4 = map(int, input().split())
v5 = v2 // v3 - (v1 - 1) // v3
v6 = v2 // v4 - (v1 - 1) // v4
v7 = v2 // f1(v3, v4) - (v1 - 1) // f1(v3, v4)
v8 = v2 - v1 + 1 - (v5 + v6 - v7)
print(v8)
