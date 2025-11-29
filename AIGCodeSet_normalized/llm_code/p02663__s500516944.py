v1, v2, v3, v4, v5 = map(int, input().split())
v6 = v3 - v1
if v2 > v4:
    v7 = 60 + v4 - v2
    v6 -= 1
else:
    v7 = v4 - v2
v8 = v6 * 60 + v7
v8 -= v5
print(v8)
