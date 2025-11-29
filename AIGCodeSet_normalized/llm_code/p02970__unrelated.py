import math
v1, v2 = map(int, input().split())
v3 = math.ceil(v1 / (2 * v2 + 1))
print(v3)
