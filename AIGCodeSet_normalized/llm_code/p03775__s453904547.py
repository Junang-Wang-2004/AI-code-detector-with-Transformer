import math
v1 = int(input())
v2 = math.inf
for v3 in range(1, 1 + math.floor(math.sqrt(v1))):
    if v1 % v3 == 0:
        v2 = min(v2, len(str(v1 // v3)))
print(v2)
