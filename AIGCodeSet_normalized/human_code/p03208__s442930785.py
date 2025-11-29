v1, v2 = list(map(int, input().strip().split()))
v3 = int(100000000000.0)
v4 = [int(input()) for v5 in range(v1)]
v4.sort()
for v5 in range(v1 - v2 + 1):
    v6 = v4[v5]
    v7 = v4[v5 + v2 - 1]
    v3 = min(v3, v7 - v6)
print(v3)
