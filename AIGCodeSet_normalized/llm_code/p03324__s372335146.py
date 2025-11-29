v1, v2 = list(map(int, input().split()))
if v1 == 0:
    print(v2)
else:
    print(v2 * 100 ** (v1 - 1))
