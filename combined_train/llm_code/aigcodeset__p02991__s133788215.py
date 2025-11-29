from collections import deque
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3[v5 - 1].append(v6 - 1)
v7, v8 = map(int, input().split())
v9 = [-1] * v1
v10 = deque([v7 - 1])
while len(v10) > 0:
    v11 = v10.popleft()
    v12 = v9[v11]
    v13 = v3[v11]
    for v5 in v13:
        if v9[v5] == -1:
            v10.append(v5)
            v9[v5] = v12 + 1
if v9[v8 - 1] == -1:
    print(-1)
else:
    print(v9[v8 - 1] // 3)
