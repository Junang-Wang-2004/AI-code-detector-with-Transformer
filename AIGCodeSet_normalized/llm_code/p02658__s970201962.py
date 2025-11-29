v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
if 0 in v2:
    print(0)
else:
    for v4 in v2:
        v3 *= v4
        if v3 > 10 ** 18:
            print(-1)
            exit()
    print(v3)
