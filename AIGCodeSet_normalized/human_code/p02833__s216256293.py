v1 = int(input())
if v1 % 2 == 0:
    v2 = v1 // 10
    v3 = 50
    while v1 >= v3:
        v2 += v1 // v3
        v3 *= 5
    print(v2)
else:
    print(0)
