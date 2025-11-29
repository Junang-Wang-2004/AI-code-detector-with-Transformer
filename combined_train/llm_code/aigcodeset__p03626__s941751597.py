v1 = int(input())
v2 = input()
v3 = input()
v4 = 0
v5 = [1, 0]
v6 = 1000000007
while v4 < v1:
    if v2[v4] == v3[v4]:
        v4 += 1
        if v5[1] in [0, 1]:
            v5[0] = v5[0] * 3 % v6
        v5[1] = 1
    else:
        v4 += 2
        if v5[1] == 0:
            v5[0] = v5[0] * 6 % v6
        elif v5[1] == 1:
            v5[0] = v5[0] * 2 % v6
        elif v5[1] == 2:
            v5[0] = v5[0] * 3 % v6
        v5[1] = 2
print(v5[0])
