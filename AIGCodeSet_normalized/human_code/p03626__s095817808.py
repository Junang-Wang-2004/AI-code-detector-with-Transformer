v1 = int(input())
v2 = input()
v3 = input()
v4 = 0
v5 = 0
v6 = 1000000007
v7 = True
while v2:
    if len(v2) > 1 and v2[0] == v2[1]:
        v2 = v2[2:]
        if v7:
            v5 = 6
            v4 = 0
            v7 = False
        else:
            v5 = v4 * 2 + v5 * 3
            v4 = 0
    else:
        v2 = v2[1:]
        if v7:
            v4 = 3
            v5 = 0
            v7 = False
        else:
            v4 = v4 * 2 + v5
            v5 = 0
    v4 %= v6
    v5 %= v6
print((v5 + v4) % v6)
