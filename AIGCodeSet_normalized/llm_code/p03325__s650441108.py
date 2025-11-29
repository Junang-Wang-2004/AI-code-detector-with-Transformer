import numpy as np
v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = 0
for v3 in range(v1):
    while v2[v3] % 2 == 0:
        v2[v3] //= 2
        v4 += 1
print(v4)
