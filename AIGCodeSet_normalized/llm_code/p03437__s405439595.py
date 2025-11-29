v1, v2 = map(int, input().split())
if v2 != 1:
    if v1 * (v2 - 1) // v2 != 0:
        print(v1 * (v2 - 1))
    else:
        print(-1)
else:
    print(v1)
