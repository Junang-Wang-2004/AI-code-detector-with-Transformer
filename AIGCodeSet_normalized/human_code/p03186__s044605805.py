v1, v2, v3 = map(int, input().split())
v4 = v2
v5 = v1 + v2
if v5 + 1 >= v3 + 1:
    v4 += v3
else:
    v4 += v5 + 1
print(v4)
