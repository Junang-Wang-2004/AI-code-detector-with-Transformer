import bisect
import sys
input = sys.stdin.readline
from collections import deque
v1 = int(input())
v2 = 0
v3 = []
for v4 in range(v1):
    v5 = int(input())
    v3.append(v5)
v6 = [-1, 10 ** 10]
v6 = deque()
v6.appendleft(10 ** 10)
v6.appendleft(-1)
for v4 in range(v1):
    if bisect.bisect_left(v6, v3[v4]) == 1:
        v6.insert(1, v3[v4])
    elif bisect.bisect_left(v6, v3[v4]) == len(v6) - 1:
        v6.insert(len(v6) - 1, v3[v4])
    else:
        v6[bisect.bisect_left(v6, v3[v4]) - 1] = v3[v4]
print(len(v6) - 2)
