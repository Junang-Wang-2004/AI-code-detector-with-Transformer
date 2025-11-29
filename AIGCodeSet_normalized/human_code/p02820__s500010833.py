from collections import deque
v1, v2 = map(int, input().split())
v3, v4, v5 = map(int, input().split())
v6 = list(input())
v7 = {'r': v3, 's': v4, 'p': v5}
v8 = {'r': 'p', 's': 'r', 'p': 's'}
v9 = deque([None] * v2)
v10 = 0
for v11 in v6:
    v12 = v9.popleft()
    if v8[v11] != v12:
        v9.append(v8[v11])
        v10 += v7[v8[v11]]
    else:
        v9.append(None)
print(v10)
