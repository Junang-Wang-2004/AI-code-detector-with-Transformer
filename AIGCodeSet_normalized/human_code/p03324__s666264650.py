v1, v2 = map(int, input().split())
if v2 < 100:
    print(100 ** v1 * v2)
else:
    print(100 ** v1 * (v2 + 1))
