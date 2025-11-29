v1, v2 = map(int, input().split())
if v2 // 2 <= v1:
    print(v2 // 2)
else:
    v2 -= v1 * 2
    print(v1 + v2 // 4)
