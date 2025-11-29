import math
v1 = int(input())
v2 = 100
v3 = 0
while v2 < v1:
    v3 += 1
    v2 += math.floor(v2 * 0.01)
print(v3)
