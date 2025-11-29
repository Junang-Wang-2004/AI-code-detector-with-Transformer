from bisect import bisect_left
from collections import deque
v1 = int(input())
v2 = int(input())
v3 = deque([v2])
for v4 in range(v1 - 1):
    v5 = int(input())
    v6 = bisect_left(v3, v5)
    if v6 == 0:
        v3.appendleft(v5)
        continue
    v3[v6 - 1] = v5
print(len(v3))
