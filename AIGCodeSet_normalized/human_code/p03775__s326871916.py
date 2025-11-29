v1 = int(input())
import math
v2 = []
for v3 in range(1, int(math.sqrt(v1) + 1)):
    if v1 % v3 == 0:
        v2.append(max(len(str(v3)), len(str(int(v1 // v3)))))
print(min(v2))
