from fractions import gcd
from functools import reduce
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 10 ** 9 + 7
v4 = reduce(lambda x, y: x * (y // gcd(x, y)), v2)
v5 = sum((v4 // x for v6 in v2))
v5 %= v3
print(v5)
