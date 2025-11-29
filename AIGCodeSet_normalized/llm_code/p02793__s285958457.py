v1 = int(input())
v2 = list(map(int, input().split()))
import fractions
v3 = v2[0]
for v4 in range(1, v1):
    v3 = v3 * v2[v4] // fractions.gcd(v3, v2[v4])
v5 = 0
for v4 in v2:
    v5 += v3 // v4
print(v5 % (10 ** 9 + 7))
