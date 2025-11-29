import math
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in v2:
    v3 = v4 * v3 // math.gcd(v3, v4)
v5 = list(map(lambda x: v3 // v4, v2))
print(int(sum(v5) % (10 ** 9 + 7)))
