import sys
import heapq
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(3 * v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5 - 1].append([v6 - 1 + v1, 1])
    v3[v5 - 1 + v1].append([v6 - 1 + 2 * v1, 1])
    v3[v5 - 1 + 2 * v1].append([v6 - 1, 1])
v7, v8 = map(int, input().split())
v9 = 10 ** 10
v10 = [v9 for v4 in range(3 * v1)]
v11 = []
v10[v7 - 1] = 0
heapq.heappush(v11, [0, v7 - 1])
while not len(v11) == 0:
    v12 = heapq.heappop(v11)
    v13 = v12[1]
    v14 = v12[0]
    if v10[v13] < v14:
        continue
    for v4 in range(len(v3[v13])):
        v15 = v3[v13][v4]
        if v10[v15[0]] > v10[v13] + v15[1]:
            v10[v15[0]] = v10[v13] + v15[1]
            heapq.heappush(v11, [v10[v15[0]], v15[0]])
if v10[v8 - 1] == v9:
    print(-1)
else:
    print(v10[v8 - 1] // 3)
