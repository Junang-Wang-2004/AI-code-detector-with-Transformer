v1 = int(input())
import math

def f1(a1, a2):
    return max(len(str(a1)), len(str(a2)))
v2 = 1000000000000.0
v3 = math.ceil(math.sqrt(v1))
for v4 in range(1, v3):
    if v1 % v4 == 0:
        v2 = min(v2, f1(v4, v1 // v4))
print(v2)
