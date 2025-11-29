import numpy as np
v1 = int(input())
v2 = list(map(int, input().split()))
if 0 in v2:
    print(0)
    exit()
v3 = 1
for v4 in range(v1):
    v3 *= v2[v4]
    if v3 > 10 ** 18:
        print(-1)
        exit()
print(v3)
