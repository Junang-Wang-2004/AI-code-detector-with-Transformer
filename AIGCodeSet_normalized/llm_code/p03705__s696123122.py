v1, v2, v3 = map(int, input().split())
if v2 > v3 or (v1 == 1 and v2 != v3):
    print(0)
else:
    print((v1 - 1) * (v3 - v2) + 1)
