from collections import deque
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
for v3 in range(v1):
    v4, v5 = v2[v3]
    v2[v3].append(v4 + v5)
v2.sort(key=lambda x: x[2], reverse=True)
v2 = deque(v2)
v6 = 0
v7 = 0
while len(v2) > 0:
    v4, v5, v8 = v2.popleft()
    if v6 % 2 == 0:
        v7 += v4
    else:
        v7 -= v5
    v6 += 1
print(v7)
