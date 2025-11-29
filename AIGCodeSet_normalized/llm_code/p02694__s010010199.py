import math
from decimal import Decimal
v1 = int(input())
v2 = 100
v3 = 0
while True:
    if v2 >= v1:
        break
    v2 = v2 * Decimal(floor(v2 * 1.01))
    v3 += 1
print(v3)
