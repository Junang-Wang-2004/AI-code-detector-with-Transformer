v1, v2 = map(int, input().split())
if v1 == 1:
    if v2 == 1:
        print(1)
    else:
        print(v2 - 2)
elif v1 == 2:
    print(0)
elif v2 == 1:
    print(v1 - 2)
elif v2 == 2:
    print(0)
else:
    print(v1 * v2 - (v1 * 2 + v2 * 2 - 4))
