v1, v2 = map(int, input().split())
if v1 >= 2 and v2 >= 2:
    print((v1 - 2) * (v2 - 2))
elif v1 == 1:
    print(v2 - 2)
else:
    print(v1 - 2)
