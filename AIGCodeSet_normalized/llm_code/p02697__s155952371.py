v1, v2 = map(int, input().split())
v3 = 1
v4 = v1
for v5 in range(v2):
    print(v3, v4)
    v3 += 1
    v4 -= 1
    if v3 > v1:
        v3 = 1
    if v4 < 1:
        v4 = v1
