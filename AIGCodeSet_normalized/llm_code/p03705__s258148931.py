v1, v2, v3 = map(int, input().split())
if v1 == 1:
    print(1)
else:
    print((v3 - v2 + 1) * v1 - (v1 - 1))
