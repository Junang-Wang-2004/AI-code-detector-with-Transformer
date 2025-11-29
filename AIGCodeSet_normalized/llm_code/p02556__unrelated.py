import sys
v1 = int(input())
v2 = 10 ** 9
v3 = 0
v4 = 10 ** 9
v5 = 0
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v2 = min(v2, v7)
    v3 = max(v3, v7)
    v4 = min(v4, v8)
    v5 = max(v5, v8)
print(abs(v3 - v2) + abs(v5 - v4))
