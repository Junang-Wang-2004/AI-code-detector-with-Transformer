v1, v2 = map(int, input().split())
if v1 == 0:
    if v2 <= 99:
        print(v2)
    else:
        print(101)
elif v1 == 1:
    if v2 <= 99:
        print(100 * v2)
    else:
        print(10100)
elif v2 <= 99:
    print(10000 * v2)
else:
    print(1010000)
