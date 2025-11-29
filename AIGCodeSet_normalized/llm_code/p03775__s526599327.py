v1 = int(input())
v2 = 999
from math import sqrt
for v3 in range(1, int(sqrt(v1)) + 1):
    if v1 % v3 == 0:
        v2 = min(v2, max(len(str(v3)), len(str(v1 // v3))))
print(v2)
