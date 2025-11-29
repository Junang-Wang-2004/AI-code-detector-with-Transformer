v1, v2, v3 = list(map(int, input().split()))
if v1 == 0 and v2 == 0:
    print(1)
elif v1 % v3 == 0:
    print(v2 // v3 - v1 // v3 + 1)
else:
    print(v2 // v3 - (v1 - 1) // v3)
