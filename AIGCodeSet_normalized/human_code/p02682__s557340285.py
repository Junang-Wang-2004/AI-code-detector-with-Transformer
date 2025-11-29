v1, v2, v3, v4 = map(int, input().split())
if v4 <= v1:
    v5 = v4 * 1
elif v1 < v4 <= v1 + v2:
    v5 = v1
elif v1 + v2 < v4 <= v1 + v2 + v3:
    v5 = v1 - (v4 - v1 - v2)
print(v5)
