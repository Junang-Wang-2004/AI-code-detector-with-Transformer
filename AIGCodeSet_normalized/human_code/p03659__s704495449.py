v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
for v5 in range(v1):
    v3 += v2[v5]
v6 = 100000000000
for v5 in range(v1 - 1):
    v4 = v4 + v2[v5]
    v7 = v3 - v4
    v6 = min(v6, abs(v4 - v7))
print(v6)
