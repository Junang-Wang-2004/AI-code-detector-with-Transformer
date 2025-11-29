v1, v2, v3 = map(int, input().split())
if v1 + v2 >= v3:
    v4 = v3 + v2
elif v1 + v2 < v3:
    v4 = v1 + v2 + v2
print(v4)
