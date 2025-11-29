v1, v2, v3 = map(int, input().split())
if v1 >= v3 - 1:
    v4 = v2 + v3
else:
    v4 = v1 + v2 + v2
print(v4)
