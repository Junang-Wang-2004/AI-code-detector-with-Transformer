from fractions import gcd

def f1(a1, a2):
    return a1 * a2 // gcd(a1, a2)
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = 1
for v5 in v3:
    v4 = f1(v4, v5)
v6 = v4 * sum([pow(s, v1 - 2, v1) for v7 in v3]) % v1
print(int(v6 % v1))
