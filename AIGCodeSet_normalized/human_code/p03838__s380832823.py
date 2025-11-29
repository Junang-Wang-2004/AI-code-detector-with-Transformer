v1, v2 = map(int, input().split())
if (v1 >= 0 and v2 >= 0 or (v1 < 0 and v2 < 0)) and v1 < v2:
    print(abs(v1 - v2))
elif (v1 >= 0 and v2 >= 0) and v2 < v1:
    print(abs(v1 - v2 + 1 + (v2 != 0)))
elif (v1 < 0 and v2 < 0) and v2 < v1:
    print(abs(v1 - v2) + 2)
elif v1 == -v2:
    print(1)
else:
    print(abs(abs(v1) - abs(v2)) + (v2 != 0))
