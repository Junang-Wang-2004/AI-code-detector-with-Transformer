v1, v2 = map(int, input().split())
if v1 == 0:
    if v2 == 100:
        print(101)
    else:
        print(v2)
elif v1 == 1:
    if v2 == 100:
        print(10100)
    else:
        print(100 * v2)
elif v1 == 2:
    if v2 == 100:
        print(1010000)
    else:
        print(10000 * v2)
