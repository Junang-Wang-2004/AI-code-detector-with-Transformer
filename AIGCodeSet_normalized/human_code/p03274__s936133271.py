v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = float('inf')
if v1 == 1:
    v4 = abs(v3[0])
for v5 in range(v1 - v2 + 1):
    v6 = v3[v5]
    v7 = v3[v5 + v2 - 1]
    v4 = min(abs(v6) + abs(v7 - v6), abs(v7) + abs(v6 - v7), v4)
print(v4)
