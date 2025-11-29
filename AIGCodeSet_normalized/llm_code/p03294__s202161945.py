import math
import fraction
from functools import reduce

def f1(a1, a2):
    return a1 * a2 // fraction.gcd(a1, a2)

def f2(a1):
    return reduce(f1, a1, 1)
v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = 0
v5 = f2(v2)
for v6 in v2:
    v4 += (v5 - 1) % v6
print(v4)
