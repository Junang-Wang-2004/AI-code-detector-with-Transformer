from collections import defaultdict
from heapq import heappop, heappush
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = defaultdict(int)
for v4 in v2:
    v3[v4] += 1
v5 = []
for v4 in list(set(v2)):
    v5.append([v4, v3[v4]])
v6 = len(v5)
v5 = sorted(v5)
v7 = 1
v8 = True
while v5[0][1] - 1 > 0:
    if v7 >= v6:
        v7 = 1
        v8 = True
    if v5[v7][1] > 1:
        v5[v7][1] -= 1
        v8 = False
        v5[0][1] -= 1
    v7 += 1
if v5[0][1] > 1:
    if v5[0][1] % 2:
        print(v6)
    else:
        print(v6 - 1)
else:
    for v7 in range(v6):
        if v5[v7][1] > 2:
            if v5[v7][1] % 2:
                v5[v7][1] = 1
            else:
                v5[v7][1] = 2
    v9 = 0
    for v7 in range(v6):
        if v5[v7][1] == 2:
            v9 += 1
    if v9 % 2:
        print(v6 - 1)
    else:
        print(v6)
