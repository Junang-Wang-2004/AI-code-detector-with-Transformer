import math
v1 = int(input())
for v2 in range(1, v1 + 1):
    if math.floor(v2 * 1.08) == v1:
        print(v2)
        break
else:
    print(':(')
