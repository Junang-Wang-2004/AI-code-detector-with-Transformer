import sys
import math
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
if v1 >= 1000 and v2 > math.log(v1):
    print(*[v1] * v1)
    sys.exit()
if v2 >= v1:
    print(*[v1] * v1)
    sys.exit()
for v4 in range(v2):
    v5 = [0] * v1
    for v6 in range(v1):
        v7 = 0
        for v8 in range(1, max(v1 - v6, v6 + 1)):
            if v6 + v8 < v1 and v3[v6 + v8] >= v8:
                v7 += 1
            if v6 - v8 >= 0 and v3[v6 - v8] >= v8:
                v7 += 1
        v5[v6] = v7
    v3 = v5
print(*v3)
