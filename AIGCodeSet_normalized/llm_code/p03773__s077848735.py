v1, v2 = map(int, input().split())
if v1 + v2 > 23:
    print((v1 + v2) % 24)
else:
    print(v1 + v2)
