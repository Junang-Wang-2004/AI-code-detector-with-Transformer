import math
v1 = int(input())
v2 = 0
for v3 in range(int(math.sqrt(v1)), 0, -1):
    if v1 % v3 == 0:
        v4 = int(v1 / v3)
        v5 = max(len(str(v3)), len(str(v4)))
        print(v5)
        break
