import math
import numpy
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = max(v2)
v4 = math.ceil(v3 / 2)
v5 = v4
v6 = v4
if v1 > 2:
    while True:
        if v5 in v2:
            v7 = v5
            break
        if v6 in v2:
            v7 = v6
            break
        else:
            v5 += 1
            v6 -= 1
else:
    v7 = min(v2)
print('{} {}'.format(v3, v7))
