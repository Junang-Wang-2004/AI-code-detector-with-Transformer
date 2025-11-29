from collections import deque
v1 = int(input())
v2 = deque()
v3 = []
for v4 in range(v1):
    v5 = int(input())
    v3.append(v5)
v3.sort()
v3 = deque(v3)
v6 = 0
v7 = 0
v8 = v3.popleft()
v2.append(v8)
while v3:
    v5 = abs(v2[0] - v3[0])
    v9 = abs(v2[0] - v3[-1])
    v10 = abs(v2[-1] - v3[-1])
    v11 = abs(v2[-1] - v3[0])
    v12 = max(v5, v9, v10, v11)
    if v5 == v12:
        v13 = v3.popleft()
        v2.appendleft(v13)
    elif v9 == v12:
        v13 = v3.pop()
        v2.appendleft(v13)
    elif v10 == v12:
        v13 = v3.pop()
        v2.append(v13)
    elif v11 == v12:
        v13 = v3.popleft()
        v2.append(v13)
v14 = 0
for v4 in range(v1 - 1):
    v14 += abs(v2[v4 + 1] - v2[v4])
print(v14)
