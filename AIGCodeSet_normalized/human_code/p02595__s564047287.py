v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v5 * v5 + v6 * v6 <= v2 * v2:
        v3 += 1
print(v3)
