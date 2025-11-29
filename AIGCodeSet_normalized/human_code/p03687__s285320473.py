v1 = input()
v2 = list(set(list(v1)))
v3 = len(v1)
for v4 in v2:
    v5 = list(v1)
    v6 = 0
    while len(set(v5)) > 1:
        for v7 in range(len(v5) - 1):
            if v5[v7 + 1] == v4:
                v5[v7] = v4
        v5.pop()
        v6 += 1
    v3 = min(v3, v6)
print(v3)
