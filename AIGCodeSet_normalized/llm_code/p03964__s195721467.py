import math
from fractions import Fraction
v1 = int(input())
v2, v3 = map(int, input().split())
v4, v5 = (v2, v3)
for v6 in range(v1 - 1):
    v7, v8 = map(int, input().split())
    '\n    if (t >= a):\n        c = math.ceil(tt / t)\n\n    else:\n        c = math.ceil(aa / a)\n    '
    v9 = math.lcm(v4, v7) // v4
    v9 = math.lcm(v5, v8) // v5
    v9 = max(v9, 1)
    v4 = v7 * v9
    v5 = v8 * v9
v10 = v4 + v5
print(v10)
