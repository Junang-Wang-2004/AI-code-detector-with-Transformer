v1, v2, v3 = map(int, input().split())
if v3 > v1:
    v1, v3 = (0, v3 - v1)
    v2 -= v3
    v2 = max(0, v2)
else:
    v1 -= v3
print(v1, v2)
