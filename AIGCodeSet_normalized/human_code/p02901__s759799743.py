import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = [float('inf')] * (1 << v1)
for v4 in range(v2):
    v5, v4 = map(int, input().split())
    v6 = list(map(int, input().split()))
    v7 = 0
    for v8 in v6:
        v7 |= 1 << v8 - 1
    v3[v7] = min(v3[v7], v5)
for v9 in range(1 << v1):
    for v10 in range(1 << v1):
        v3[v9 | v10] = min(v3[v9 | v10], v3[v9] + v3[v10])
v11 = v3[-1]
print(v11 if v11 != float('inf') else -1)
