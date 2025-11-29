v1, v2, v3 = map(int, input().strip().split(' '))
if v2 > v3:
    print(v2 + v3)
elif v1 + v2 > v3:
    print(v2 + v3)
else:
    print(v1 + 2 * v2 + 1)
