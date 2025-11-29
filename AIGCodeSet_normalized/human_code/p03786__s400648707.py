import numpy as np
v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = np.cumsum(v2)[::-1]
v2 = v2[::-1]
v4 = 1
for v5 in range(v1 - 1):
    if v2[v5] <= v3[v5 + 1] * 2:
        v4 += 1
    else:
        break
print(v4)
