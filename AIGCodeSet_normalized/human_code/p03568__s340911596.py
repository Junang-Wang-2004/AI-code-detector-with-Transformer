v1 = int(input())
*v2, = map(int, input().split())
from itertools import product
v3 = 0
for v4 in product(range(3), repeat=v1):
    v5 = 0
    for v6 in range(v1):
        v7 = v2[v6] + v4[v6] - 1
        v5 |= v7 % 2 == 0
    if v5:
        v3 += 1
print(v3)
