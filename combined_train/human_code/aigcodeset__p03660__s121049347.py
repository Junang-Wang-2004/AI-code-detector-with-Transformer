v1 = int(input())
v2 = [[] for v3 in range(v1)]
for v3 in range(v1 - 1):
    v4, v5 = tuple(map(lambda x: int(x) - 1, input().split()))
    v2[v4].append(v5)
    v2[v5].append(v4)
v6 = [0] * v1
v6[0] = 1
v6[v1 - 1] = -1
from collections import deque
v7 = deque([])
v7.append(0)
v7.append(v1 - 1)
while v7:
    v8 = v7.popleft()
    v9 = v6[v8]
    for v10 in v2[v8]:
        if v6[v10] == 0:
            v6[v10] = v9
            v7.append(v10)
v11 = v6.count(1)
v12 = v6.count(-1)
if v11 > v12:
    print('Fennec')
else:
    print('Snuke')
