import math
from collections import Counter
v1, v2 = map(int, input().split())
v3 = math.gcd(v1, v2)
v4 = Counter()
for v5 in range(2, math.ceil(math.sqrt(v3)) + 1):
    while v3 % v5 == 0:
        v3 //= v5
        v4[v5] += 1
if v3 > 1:
    v4[int(v3)] += 1
print(len(v4) + 1)
