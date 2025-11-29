v1, v2, v3 = map(int, input().split())
if v1 + v2 >= v3 - 1:
    print(v3 + v2)
else:
    print(v1 + v1 + v2 + 1)
