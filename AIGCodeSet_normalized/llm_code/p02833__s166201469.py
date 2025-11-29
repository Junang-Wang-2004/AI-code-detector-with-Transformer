v1 = int(input())
if v1 % 2 == 1:
    print(0)
else:
    v2 = 0
    v3 = 10
    while v1 // v3 > 0:
        v2 += v1 // v3
        v3 *= 5
    print(v2)
