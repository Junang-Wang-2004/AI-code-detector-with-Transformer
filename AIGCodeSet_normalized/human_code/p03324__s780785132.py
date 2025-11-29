v1, v2 = map(int, input().split())
if v2 < 100:
    v3 = 100 ** v1 * v2
else:
    v3 = 100 ** v1 * (v2 + 1)
print(v3)
