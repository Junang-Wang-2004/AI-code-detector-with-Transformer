v1 = input().split()
v2 = int(v1[0])
v3 = int(v1[1])
v4 = 0
for v5 in range(v2, v3 + 1):
    v6 = str(v5)
    if v6[0] == v6[-1]:
        if v6[1] == v6[-2]:
            v4 += 1
print(v4)
