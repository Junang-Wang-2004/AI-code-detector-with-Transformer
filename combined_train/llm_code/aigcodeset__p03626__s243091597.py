v1 = 1000000007
v2 = int(input())
v3 = input()
v4 = input()
v5 = 1
v6 = 0
v7 = None
if v3[v6] == v4[v6]:
    v5 *= 3
    v6 += 1
    v7 = 0
else:
    v5 *= 6
    v6 += 2
    v7 = 1
while v6 < len(v3) - 1:
    if v3[v6] == v4[v6]:
        if v7:
            v5 *= 1
        else:
            v5 *= 2
        v6 += 1
        v7 = 0
    else:
        if v7:
            v5 *= 3
        else:
            v5 *= 2
        v6 += 2
        v7 = 1
print(v5 % v1)
