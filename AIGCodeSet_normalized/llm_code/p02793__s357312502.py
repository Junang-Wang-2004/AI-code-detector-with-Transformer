import fractions
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = list(map(int, input().split()))
if v2 == 1:
    print(v3[0])
    exit()
v4 = fractions.gcd(v3[0], v3[1])
v5 = v3[0] * v3[1] // v4
v6 = v3[0] // v4 + v3[1] // v4
for v7 in range(2, v2):
    v8 = fractions.gcd(v5, v3[v7])
    v4 = v3[v7] // v8 % v1
    v5 = v5 * v3[v7] // v8
    v6 *= v4
    v6 += v5 // v3[v7]
    v6 %= v1
print(v6)
