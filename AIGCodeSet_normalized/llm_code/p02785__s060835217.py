v1, v2 = map(int, input().strip().split())
v3 = list(map(int, input().strip().split()))
v3 = sorted(v3, reverse=True)
v4 = 0
for v5 in range(v2, v1):
    v4 += v3[v5]
for v5 in range(v2):
    if v3[v5] > 0:
        v4 += v3[v5] - 1
print(v4)
