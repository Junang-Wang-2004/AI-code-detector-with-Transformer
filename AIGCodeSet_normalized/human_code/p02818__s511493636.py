v1, v2, v3 = map(int, input().split())
if v1 < v3:
    v2 = max(v2 - (v3 - v1), 0)
    v1 = 0
else:
    v1 = v1 - v3
print(v1, end=' ')
print(v2)
