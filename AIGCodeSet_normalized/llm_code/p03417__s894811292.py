v1, v2 = map(int, input().split())
if v1 >= 2 and v2 >= 2:
    print(v1 * v2 - (v1 - 2) * (v2 - 2))
else:
    print(0)
