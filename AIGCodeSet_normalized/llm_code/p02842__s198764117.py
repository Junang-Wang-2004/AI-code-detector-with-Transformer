import math
v1 = int(input())
v2 = math.floor(v1 / 1.08)
if v1 == v2 * 1.08:
    print(v2)
else:
    print(':(')
