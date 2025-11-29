v1, v2, v3 = map(int, input().split())
v4 = v1 - v2
v5 = v3 - v4
if v5 < 0:
    print(0)
if v5 >= 0:
    print(v5)
