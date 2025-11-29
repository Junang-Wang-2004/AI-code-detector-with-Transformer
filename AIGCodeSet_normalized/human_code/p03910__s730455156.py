import sys
import math
v1 = int(sys.stdin.readline())
v2 = int(math.ceil((math.sqrt(1 + 8 * v1) - 1) / 2))
v3 = int(v2 * (v2 + 1) / 2 - v1)
for v4 in range(v2):
    v4 = v4 + 1
    if v3 != v4:
        print(v4)
