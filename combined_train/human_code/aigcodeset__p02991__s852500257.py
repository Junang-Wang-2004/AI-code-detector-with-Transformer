from collections import deque
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5 - 1].append(v6 - 1)
v7, v8 = map(int, input().split())
v7 -= 1
v8 -= 1
v9 = {}
v10 = deque()
v10.append((v7, 0))
v11 = -1
while v10:
    v12, v13 = v10.popleft()
    if v12 in v9 and v13 % 3 in v9[v12]:
        continue
    if v12 not in v9:
        v9[v12] = set()
    v9[v12].add(v13 % 3)
    for v14 in v3[v12]:
        if v14 == v8 and v13 % 3 == 2:
            v11 = v13 + 1
            break
        v10.append((v14, v13 + 1))
    if v11 % 3 == 0:
        break
if v11 == -1:
    print(-1)
else:
    print(v11 // 3)
