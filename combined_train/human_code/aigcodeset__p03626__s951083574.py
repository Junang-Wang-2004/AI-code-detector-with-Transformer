v1 = int(input())
v2 = input()
v3 = input()
v4 = 0
v5 = 1
v6 = int(1000000000.0) + 7
v7 = True
while v4 < v1:
    if v2[v4] == v3[v4]:
        if v4 == 0:
            v5 = 3
        elif v7:
            v5 *= 2
            v5 %= v6
        else:
            v5 *= 1
        v7 = True
        v4 += 1
    else:
        if v4 == 0:
            v5 = 6
        elif v7:
            v5 *= 2
        else:
            v5 *= 3
            v5 %= v6
        v7 = False
        v4 += 2
print(v5)
