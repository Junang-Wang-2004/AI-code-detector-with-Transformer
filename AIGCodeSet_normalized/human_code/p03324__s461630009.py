v1, v2 = [int(i) for v3 in input().split()]
if v2 == 100:
    if v1 == 0:
        print(v2 + 1)
    elif v1 == 1:
        print(100 ** 2 + 100)
    else:
        print(100 ** 3 + 100 ** 2)
elif v1 == 0:
    print(v2)
else:
    print(100 ** v1 * v2)
