v1, v2, v3, v4 = map(int, input().split())
if v3 <= v2:
    if v2 <= v4:
        print(v2 - v3)
    else:
        print(v4 - v3)
else:
    print(0)
