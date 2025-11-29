v1 = int(input())
sum = 0
v2 = ''
if v1 < 0:
    v3 = abs(v1)
    if v3 % 2 == 1:
        v3 = v3 + 1
        print(str(bin(v3))[2:-1] + '1')
    else:
        print(str(bin(v3))[2:-1])
elif v1 > 0:
    while v1 != 1:
        if v1 % -2 == -1:
            v2 = v2 + '1'
            v1 = v1 - 1
            v1 = v1 / -2
        else:
            v2 = v2 + '0'
            v1 = v1 / -2
    v2 = v2 + '1'
    for v4 in range(len(v2)):
        print(v2[len(v2) - 1 - v4], end='')
    print()
else:
    print(0)
