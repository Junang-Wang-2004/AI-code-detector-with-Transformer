from fractions import gcd
v1 = int(input())
v2 = list(map(int, input().split(' ')))
v3 = 0
v4 = 1
v5 = 1
v6 = 10 ** 9 + 7

def f1(a1, a2):
    return a1 * a2 // gcd(a1, a2)
for v7 in v2[:v1 // 2]:
    v4 = f1(v4, v7)
for v8 in v2[v1 // 2:]:
    v5 = f1(v5, v8)
v9 = f1(v4, v5)
v10 = sum([v4 // v7 for v7 in v2[:v1 // 2]])
v11 = sum([v5 // v7 for v7 in v2[v1 // 2:]])
v10 *= v9 // v4
v11 *= v9 // v5
print((v10 + v11) % v6)
