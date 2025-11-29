v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum(v2)
v4 = float('inf')
v5 = 0
for v6 in range(1, v1):
    v5 += v2[v6 - 1]
    v7 = v3 - v5
    v8 = abs(v5 - v7)
    v4 = min(v4, v8)
print(v4)
