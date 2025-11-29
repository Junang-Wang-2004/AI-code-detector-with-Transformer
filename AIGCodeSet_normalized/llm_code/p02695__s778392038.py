v1, v2, v3 = map(int, input().split())
v4 = 0
if v2 < v3:
    v3 = v2
v5 = int(v2 / v1)
if v5 > v3:
    print(0)
    exit()
for v6 in range(v5, v3 + 1, v5):
    v7 = int(v1 * v6 / v2) - v1 * int(v6 / v2)
    v4 = max(v7, v4)
print(v4)
