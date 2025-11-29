v1, v2 = map(int, input().split())
if v1 * v2 == 0:
    if v1 < 0:
        print(-v1)
    elif v1 > 0:
        print(1 + v1)
    elif v2 >= 0:
        print(v2)
    else:
        print(1 - v2)
elif v1 * v2 > 0:
    if v1 > v2:
        print(2 + abs(v1 - v2))
    else:
        print(abs(v2 - v1))
else:
    print(1 + abs(v1 + v2))
