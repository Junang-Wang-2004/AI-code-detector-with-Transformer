v1, v2 = map(int, input().split())
if v1 < 10:
    print(v2 + 100 * (10 - v1))
else:
    print(v2)
