from collections import deque
v1 = int(input())
v2 = deque(map(int, input().split()))
v3 = deque(map(int, input().split()))
v4 = 0
v5 = 0
while len(v2) > 0:
    v6 = v2.popleft()
    v7 = min(v6, v5)
    v4 += v7
    v6 -= v7
    if len(v3) > 0:
        v8 = v3.popleft()
        v9 = min(v6, v8)
        v4 += v9
        v6 -= v9
        v5 = v8 - v9
print(v4)
