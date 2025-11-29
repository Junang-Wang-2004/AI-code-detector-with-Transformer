v1, v2 = map(int, input().split())
if v1 < 10:
    v3 = 100 * (10 - v1)
else:
    v3 = 0
print(v2 + v3)
