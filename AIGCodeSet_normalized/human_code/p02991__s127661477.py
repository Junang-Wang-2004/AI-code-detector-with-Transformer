import collections
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1 + 1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5].append(v6)
v7, v8 = map(int, input().split())
v9 = [[0] * 3 for v4 in range(v1 + 1)]
v9[v7][0] = 1
v10 = collections.deque()
v10.append([v7, 0])
v11 = 0
while len(v10) != 0:
    v12, v13 = v10.popleft()
    if v12 == v8 and v13 % 3 == 0:
        v11 = v13 // 3
        break
    for v14 in v3[v12]:
        if v9[v14][(v13 + 1) % 3] == 0:
            v10.append([v14, v13 + 1])
            v9[v14][(v13 + 1) % 3] = 1
if v11 == 0:
    print(-1)
else:
    print(v11)
