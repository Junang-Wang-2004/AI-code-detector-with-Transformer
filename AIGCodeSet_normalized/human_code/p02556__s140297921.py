from collections import deque
v1 = int(input())
v2, v3, v4, v5 = (-1 * 10 ** 9 * 2, 10 ** 9 * 2, -1 * 10 ** 9 * 2, 10 ** 9 * 2)
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v2 = max(v2, v7 + v8)
    v3 = min(v3, v7 + v8)
    v4 = max(v4, v7 - v8)
    v5 = min(v5, v7 - v8)
print(max(v2 - v3, v4 - v5))
