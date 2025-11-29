v1, v2, v3 = map(int, input().split())
if v1 <= 0 or v2 > v3:
    v4 = 0
elif v1 == 1:
    if v2 == v3:
        v4 = 1
    else:
        v4 = 0
elif v1 >= 2:
    v4 = v3 * (v1 - 2) - v2 * (v1 - 2) + 1
print(v4)
