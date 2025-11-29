v1, v2 = map(int, input().split())
if v1 > v2:
    v3 = v1
    v1 = v2
    v2 = v3
if v1 == 1 and v2 == 1:
    print(1)
elif v1 == 1 and v2 >= 2:
    print(v2 - 2)
elif v1 >= 2 and v2 >= 2:
    print((v1 - 2) * (v2 - 2))
