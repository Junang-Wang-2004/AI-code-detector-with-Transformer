import math
input()
v1, *v2 = map(int, input().split())
for v3 in v2:
    v1 = math.gcd(v1, v3)
print(v1)
