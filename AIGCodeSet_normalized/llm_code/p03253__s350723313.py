import math
from scipy.special import comb
v1, v2 = map(int, input().split(' '))
v3 = int(math.sqrt(v2))
v4 = 10 ** 9 + 7
v5 = {}
for v6 in range(2, v3 + 2):
    v7 = 0
    while v2 % v6 == 0:
        v2 = int(v2 / v6)
        v7 += 1
    if v7 > 0:
        v5[v6] = v7
        if v2 == 1:
            break
v8 = 1
v9 = v5.values()
for v6 in v9:
    v8 = v8 * comb(v1 - 1 + v6, v1 - 1, exact=True) % v4
print(v8 % v4)
