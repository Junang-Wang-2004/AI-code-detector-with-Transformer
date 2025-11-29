v1 = int(input())
v2 = input()
v3 = input()
v4 = 0
v5 = 0
v6 = 1
while v5 < v1:
    if v2[v5] == v3[v5]:
        if v4 == 0:
            v6 *= 3
        elif v4 == 'x':
            v6 *= 2
        v4 = 'x'
        v6 %= 10 ** 9 + 7
        v5 += 1
    else:
        if v4 == 0:
            v6 *= 6
        elif v4 == 'x':
            v6 *= 2
        else:
            v6 *= 3
        v4 = 'y'
        v6 %= 10 ** 9 + 7
        v5 += 2
print(v6)
