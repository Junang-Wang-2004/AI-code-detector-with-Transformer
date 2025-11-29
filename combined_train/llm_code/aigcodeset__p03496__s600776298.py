import numpy as np
v1 = int(input())
v2 = [int(i) for v3 in input().split(' ')]
if abs(max(v2)) >= abs(min(v2)):
    v4 = max(v2)
    v5 = np.argmax(v2)
    v6 = min(v2)
    v7 = np.argmin(v2)
else:
    v6 = min(v2)
    v7 = np.argmin(v2)
    v4 = max(v2)
    v5 = np.argmax(v2)
if v4 == 0:
    for v3 in range(v1):
        if v2[v3] > 0:
            v2[v3] = v2[v3] + v6
            print(v7 + 1, v3 + 1)
    for v3 in reversed(range(1, v1)):
        if v2[v3 - 1] > v2[v3]:
            v2[v3 - 1] = v2[v3 - 1] + v2[v3]
            print(v3 + 1, v3)
else:
    for v3 in range(v1):
        if v2[v3] < 0:
            v2[v3] = v2[v3] + v4
            print(v5 + 1, v3 + 1)
    for v3 in range(1, v1):
        if v2[v3 - 1] > v2[v3]:
            v2[v3] = v2[v3] + v2[v3 - 1]
            print(v3, v3 + 1)
