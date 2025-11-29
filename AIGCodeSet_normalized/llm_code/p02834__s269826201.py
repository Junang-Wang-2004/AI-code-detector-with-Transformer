v1, v2, v3 = map(int, input().split())
from collections import deque
v4 = [[] for v5 in range(v1)]
for v6 in range(v1 - 1):
    v7, v8 = map(int, input().split())
    v4[v7 - 1].append(v8 - 1)
    v4[v8 - 1].append(v7 - 1)

def f1(a1):
    v1 = deque([])
    v2 = [-1] * v1
    v2[a1 - 1] = 0
    v1.append(a1 - 1)
    while v1:
        v3 = v1.popleft()
        for v4 in v4[v3]:
            if v2[v4] == -1:
                v2[v4] = v2[v3] + 1
                v1.append(v4)
    return v2
v9 = f1(v2)
v10 = f1(v3)
v11 = []
for v6 in range(v1):
    if len(v4[v6]) == 1 and v9[v6] <= v10[v6]:
        v11.append(v6)
max = -1
v12 = -1
for v6 in v11:
    if v9[v6] > max:
        max = v9[v6]
        v12 = v6
print(v10[v12])
