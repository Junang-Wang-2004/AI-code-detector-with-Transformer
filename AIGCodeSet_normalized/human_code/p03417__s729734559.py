v1 = list(map(int, input().split()))
if 1 in v1:
    if max(v1) - 2 >= 0:
        print(max(v1) - 2)
    else:
        print(1)
elif 2 in v1:
    print(0)
else:
    print(v1[0] * v1[1] - (2 * v1[0] + 2 * v1[1] - 4))
