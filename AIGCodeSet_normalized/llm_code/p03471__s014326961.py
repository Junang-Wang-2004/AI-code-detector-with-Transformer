v1, v2 = map(int, input().split())
v2 = v2 / 1000
v3 = 0
for v4 in range(v1 + 1):
    for v5 in range(v1 - v4 + 1):
        if 10 * v4 + 5 * v5 + (v1 - v4 - v5) == v2:
            print(v4, v5, v1 - v4 - v5)
            v3 = 1
            break
    if v3 == 1:
        break
if v3 == 0:
    print(-1, -1, -1)
