v1, v2, v3 = map(int, input().split())
v4 = 0
for v5 in range(v1 // (v2 + v3) + 1):
    if v5 * (v2 + v3) + v2 <= v1:
        v4 = v5
print(v4)
