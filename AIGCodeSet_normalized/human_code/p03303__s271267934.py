import math
v1 = input()
v2 = int(input())
v3 = list(v1)
v4 = len(v1)
for v5 in range(math.ceil(v4 / v2)):
    print(v3[v5 * v2], end='')
