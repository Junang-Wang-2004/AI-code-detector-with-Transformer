v1 = int(input())
v2 = list(map(int, input().split()))
import math
from functools import reduce

def f1(a1, a2):
    return a1 * a2 // math.gcd(a1, a2)

def f2(*a1):
    return reduce(f1, a1, 1)
v3 = f2(*v2)
v3 = v3 - 1
v4 = 0
for v5 in v2:
    v4 += v3 % v5
print(v4)
