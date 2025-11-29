from fractions import gcd
v1 = input()
v2 = list(map(int, input().split()))
v3 = 1
for v4 in v2:
    v3 = v3 * v4 // gcd(v3, v4)
v5 = 0
for v6 in v2:
    v5 += v3 // v6
print(v5 % (10 ** 9 + 7))
