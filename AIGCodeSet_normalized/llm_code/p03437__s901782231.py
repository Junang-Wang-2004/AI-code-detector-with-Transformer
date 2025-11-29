import math
v1, v2 = map(int, input().split())
v3 = v1 * v2 // math.gcd(v1, v2)
v3 -= v1
if v3 > 0 and v3 <= 10 ** 18:
    print(int(v3))
else:
    print(-1)
