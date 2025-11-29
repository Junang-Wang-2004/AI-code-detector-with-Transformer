v1, v2, v3 = map(int, input().split())
v4 = 0
for v5 in range(v1 - 1):
    v4 += max(v2 * (x[v5 + 1] - x[v5]), v3)
print(v4)
