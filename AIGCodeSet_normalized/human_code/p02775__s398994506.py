v1 = input()
v2 = [0] * (len(v1) + 1)
v3 = 0
for v4 in range(len(v1)):
    v2[v4] = int(v1[len(v1) - 1 - v4])
for v4 in range(len(v2)):
    if v2[v4] < 5:
        v3 += v2[v4]
    elif v2[v4] == 5:
        if v2[v4 + 1] >= 5:
            v3 += 10 - v2[v4]
            v2[v4 + 1] += 1
        else:
            v3 += 5
    else:
        v3 += 10 - v2[v4]
        v2[v4 + 1] += 1
print(v3)
