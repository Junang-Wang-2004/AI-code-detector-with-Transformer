import math
v1 = int(input())
while v1 >= 1:
    max = math.ceil((-1 + (1 + 8 * v1) ** 0.5) / 2)
    print(max)
    v1 -= max
