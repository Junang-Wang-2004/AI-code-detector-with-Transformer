v1, v2, v3, v4 = list(map(int, input().split()))
if (v2 and v4) <= 0:
    print(v1 * v3)
elif (v2 or v4) <= 0:
    print(v1 * v4)
else:
    print(v4 * v2)
