v1 = input()
v2 = int(input())
v3 = ''
v4 = 0
v5 = 0
v6 = 0
v7 = 0
while v1[0] == v1[v4]:
    v6 += 1
    v4 += 1
v4 = len(v1) - 1
while v1[v4] == v1[len(v1) - 1]:
    v7 += 1
    v4 -= 1
v4 = 0
while v4 < len(v1) - 2:
    if v1[v4] == v1[v4 + 1]:
        if v4 == len(v1) - 2:
            v5 += 1
            v4 += 1
        if v1[v4 + 1] == v1[v4 + 2]:
            v5 += 1
            v4 += 2
        else:
            v5 += 1
            v4 += 1
    else:
        v4 += 1
if v4 == len(v1) - 2:
    if v1[v4] == v1[v4 + 1]:
        v5 += 1
    if v1[0] == v1[len(v1) - 1]:
        if (v6 + v7) % 2 != 0:
            v5 += 1
print(v5 * v2)
