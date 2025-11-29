v1 = int(input())
v2 = list(str(input()))
v3 = 0
for v4 in range(1000):
    v5 = list(str(v4).zfill(3))
    v6 = 0
    for v7 in range(v1):
        if v2[v7] == v5[v6]:
            v6 += 1
            if v6 == 3:
                break
    if v6 == 3:
        v3 += 1
print(v3)
