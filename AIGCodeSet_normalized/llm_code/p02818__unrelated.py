v1, v2, v3 = map(int, input().split())
if v3 <= v1:
    v1 -= v3
else:
    v1 = 0
    v3 -= v1
    if v3 <= v2:
        v2 -= v3
print(v1, v2)
