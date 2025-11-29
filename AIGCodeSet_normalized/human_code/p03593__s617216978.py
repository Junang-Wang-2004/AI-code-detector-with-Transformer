from sys import stdin
import string
import heapq
v1, v2 = map(int, stdin.readline().rstrip().split())
v3 = ''
for v4 in range(v1):
    v3 += stdin.readline().rstrip()
v5 = v1 // 2 * (v2 // 2)
v6 = v1 % 2 * (v2 // 2) + v2 % 2 * (v1 // 2)
v7 = v1 % 2 * (v2 % 2)
v8 = string.ascii_lowercase
v9 = [-v3.count(v4) for v4 in v8 if v3.count(v4) != 0]
heapq.heapify(v9)
for v4 in range(v5):
    if v9[0] <= -4:
        v10 = heapq.heappop(v9)
        if v10 + 4 == 0:
            continue
        else:
            heapq.heappush(v9, v10 + 4)
    else:
        print('No')
        exit()
for v4 in range(v6):
    if v9[0] <= -2:
        v10 = heapq.heappop(v9)
        if v10 + 2 == 0:
            continue
        else:
            heapq.heappush(v9, v10 + 2)
    else:
        print('No')
        exit()
for v4 in range(v7):
    if v9[0] <= -1:
        v10 = heapq.heappop(v9)
        if v10 + 1 == 0:
            continue
        else:
            heapq.heappush(v9, v10 + 1)
    else:
        print('No')
        exit()
print('Yes')
