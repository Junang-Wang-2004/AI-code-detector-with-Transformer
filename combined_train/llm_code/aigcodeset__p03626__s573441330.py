v1 = int(input())
v2 = input()
v3 = input()
v4 = 10 ** 9 + 7
if v1 == 1:
    v5 = 3
elif v1 == 2 or v1 == 3:
    v5 = 6
else:
    v5 = 6
    for v6 in range(3, v1):
        if v2[v6] == v3[v6]:
            if v2[v6 - 1] == v3[v6 - 1]:
                v5 = v5 * 2 % v4
            else:
                pass
        elif v2[v6 - 1] == v3[v6 - 1]:
            v5 = v5 * 2 % v4
        elif v2[v6 - 1] != v2[v6]:
            v5 = v5 * 3 % v4
        else:
            pass
print(v5)
