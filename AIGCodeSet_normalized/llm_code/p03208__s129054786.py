v1, v2 = map(int, input().split())
v3 = [int(input()) for v4 in range(v1)]
v3.sort()
v5 = float('inf')
for v6 in range(v1 - v2 + 1):
    v5 = min(v5, max(v3[v6:v6 + v2]) - min(v3[v6:v6 + v2]))
print(v5)
