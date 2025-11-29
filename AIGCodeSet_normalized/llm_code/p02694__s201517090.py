import math
v1 = int(input())
v2 = 0
v3 = 100
while v3 < v1:
    v3 = math.floor(v3 * 1.01)
    v2 += 1
print(v2)
