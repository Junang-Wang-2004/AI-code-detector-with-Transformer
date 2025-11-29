v1 = [int(s) for v2 in input()]
v3 = 0
if v1[0] == 0:
    for v2 in range(1, len(v1) - 1):
        if v2 % 2 == 0:
            if v1[v2] != 0:
                v3 += 1
        elif v1[v2] != 1:
            v3 += 1
else:
    for v2 in range(1, len(v1) - 1):
        if v2 % 2 == 0:
            if v1[v2] != 1:
                v3 += 1
            elif v1[v2] != 0:
                v3 += 1
print(v3)
