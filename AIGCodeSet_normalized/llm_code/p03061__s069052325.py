import numpy as np
v1 = int(input())
v2 = np.array([int(i) for v3 in input().split()])
v4 = 0
for v3 in range(1, 10 ** 9 + 1):
    v5 = v2.copy()
    v5[0] = v3
    v6 = np.gcd.reduce(v5)
    if v6 > v4:
        v4 = v6
print(v4)
