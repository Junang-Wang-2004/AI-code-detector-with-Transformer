import math
v1 = int(input())
v2 = v1 / 1.08
v2 = math.floor(v2)
if math.floor(v2 * 1.08) == v1:
    print(v2)
elif math.floor((v2 + 1) * 1.08) == v1:
    print(v2 + 1)
else:
    print(':(')
