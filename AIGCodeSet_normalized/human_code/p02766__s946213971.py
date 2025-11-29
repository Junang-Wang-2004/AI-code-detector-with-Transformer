import math
v1, v2 = map(int, input().split())
v3 = int(math.log(v1, v2)) + 1
print(v3)
