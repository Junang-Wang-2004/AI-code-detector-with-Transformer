v1 = int(input())
v2 = input()
v3 = input()
if len(v2) == 2:
    print(3)
    exit()
v4 = 0
v5 = []
while v4 < v1:
    try:
        if v2[v4] == v2[v4 + 1] or v3[v4] == v3[v4 + 1]:
            v5.append(1)
            v4 += 1
        else:
            v5.append(0)
        v4 += 1
    except:
        break
v6 = 1
if v5[0] == 0:
    v6 = 3
else:
    v6 = 6
v7 = 10 ** 9 + 7
for v8 in range(1, len(v5)):
    if v5[v8] == 0:
        if v5[v8 - 1] == 0:
            v6 *= 2
    elif v5[v8 - 1] == 1:
        v6 *= 3
    else:
        v6 *= 2
    v6 %= v7
print(v6)
