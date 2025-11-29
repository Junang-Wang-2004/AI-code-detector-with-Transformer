from collections import deque
v1 = int(input())
v2 = [[] for v3 in range(v1)]
v4 = [-1] * v1
for v3 in range(v1 - 1):
    v5, v6 = map(int, input().split())
    v2[v5 - 1].append(v6 - 1)
    v2[v6 - 1].append(v5 - 1)
v7 = sorted([int(a) for v8 in input().split()])
print(sum(v7) - max(v7))
v9 = deque([0])
while v9:
    v3 = deque.popleft(v9)
    if v4[v3] < 0:
        v4[v3] = v7.pop()
        for v8 in v2[v3]:
            deque.append(v9, v8)
print(*v4)
