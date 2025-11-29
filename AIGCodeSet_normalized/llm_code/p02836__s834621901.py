v1 = input()
v2 = len(v1)
v3 = 0
if v2 != 1:
    for v4 in range(int(v2 / 2)):
        if v1[v4] != v1[v2 - 1 - v4]:
            v3 += 1
    print(v3)
else:
    print(v3)
