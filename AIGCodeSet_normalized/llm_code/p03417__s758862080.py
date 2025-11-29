v1, v2 = map(int, input().split())
if v1 > v2:
    v1, v2 = (v2, v1)
if v1 == 1:
    if v2 == 1:
        print(1)
    else:
        print(v2 - 2)
else:
    print((v2 - 2) * (v1 - 2))
