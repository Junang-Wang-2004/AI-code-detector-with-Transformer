v1 = int(input())
v2 = []
for v3 in range(65):
    for v4 in range(65):
        v5 = v3 ** 5 - v4 ** 5
        if v5 == v1:
            v2.append(v3)
            v2.append(v4)
            break
    if len(v2) > 0:
        break
if len(v2) == 0:
    for v6 in range(50, 100):
        for v7 in range(v6 - 10):
            v5 = v6 ** 5 - v7 ** 5
            if v5 == v1:
                v2.append(v6)
                v2.append(v7)
                break
        if len(v2) > 0:
            break
print(v2[0], v2[1])
