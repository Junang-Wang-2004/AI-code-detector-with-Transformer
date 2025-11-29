v1, v2, v3 = map(int, input().split())
v4 = 0
v5 = 0
if v2 > v3:
    v5 = v3
else:
    v5 = v2
if v1 == v2 and v1 == v3:
    v4 = v1
elif v1 < v2 + v3:
    if v1 == v2 or v1 == v3:
        v4 = min(v2, v3)
    else:
        v4 = max(v2, v3) - min(v2, v3)
print(v5, v4)
