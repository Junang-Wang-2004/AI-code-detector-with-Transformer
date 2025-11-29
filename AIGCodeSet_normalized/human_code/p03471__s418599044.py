import math
v1, v2 = map(int, input().split())
v3 = False
for v4 in range(v1 + 1):
    for v5 in range(v1 + 1 - v4):
        v6 = v1 - v4 - v5
        v7 = v6 * 10000 + v5 * 5000 + v4 * 1000
        if v7 == v2:
            print(v6, v5, v4)
            v3 = True
            break
    if v3:
        break
if not v3:
    print(-1, -1, -1)
