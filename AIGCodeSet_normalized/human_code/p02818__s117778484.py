v1, v2, v3 = map(int, input().split())
if v1 >= v3:
    print(v1 - v3, v2)
elif v1 < v3 < v1 + v2:
    print(0, v2 - v3 + v1)
else:
    print(0, 0)
