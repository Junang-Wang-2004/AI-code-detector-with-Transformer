v1, v2, v3 = map(int, input().split())
v4 = 0
for v5 in range(1, v3 + 2):
    if v5 * v1 <= v3 + 0.5:
        v4 += v2
print(v4)
