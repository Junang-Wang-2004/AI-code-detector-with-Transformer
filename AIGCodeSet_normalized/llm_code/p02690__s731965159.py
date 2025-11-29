v1 = int(input())
v2 = int(v1 ** (1 / 5))
if v2 ** 5 < v1:
    v3 = v1 - v2 ** 5
    v4 = -int(v3 ** (1 / 5))
else:
    v3 = v2 ** 5 - v1
    v4 = int(v3 ** (1 / 5))
print(v2, v4)
