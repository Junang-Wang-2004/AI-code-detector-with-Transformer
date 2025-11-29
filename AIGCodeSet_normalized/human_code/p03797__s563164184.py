v1, v2 = map(int, input().split())
if v1 * 2 >= v2:
    print(v2 // 2)
else:
    v3 = v2 - v1 * 2
    print(v1 + v3 // 4)
