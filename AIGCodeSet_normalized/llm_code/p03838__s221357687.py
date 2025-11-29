v1, v2 = map(int, input().split())
if v2 >= v1:
    print(v2 - v1)
elif v2 == -v1:
    print(1)
elif v2 < v1 < 0:
    print(v1 - v2 + 2)
elif 0 <= v1 < v2:
    print(v2 - v1 + 1)
else:
    print(0)
