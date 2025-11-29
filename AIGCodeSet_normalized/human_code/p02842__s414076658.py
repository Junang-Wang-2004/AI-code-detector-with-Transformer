import math
v1 = int(input())
v2 = v1
v1 /= 1.08
v1 = math.ceil(v1)
if int(v1 * 1.08) == v2:
    print(v1)
else:
    print(':(')
