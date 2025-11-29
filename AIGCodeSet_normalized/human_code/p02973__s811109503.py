v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
from bisect import bisect_left
from collections import deque
v4 = deque()
for v5 in v2:
    v3 = bisect_left(v4, v5)
    if v3 == 0:
        v4.appendleft(v5)
    else:
        v4[v3 - 1] = v5
print(len(v4))
