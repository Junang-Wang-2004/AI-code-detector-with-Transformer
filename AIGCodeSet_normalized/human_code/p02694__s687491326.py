import math
v1 = int(input())
v2 = 100
for v3 in range(3761):
    if v2 < v1:
        v2 = math.floor(v2 * 1.01)
    else:
        print(v3)
        break
