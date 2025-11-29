v1, v2, v3 = map(int, input().split())
if v1 + v2 >= v3:
    print(v2 + v3)
elif v1 + v2 + 1 <= v3:
    print(v1 + 2 * v2 + 1)
else:
    print(v1 + v2)
