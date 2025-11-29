v1 = input()
v2 = input()
v3 = []
for v4 in range(len(v1) - len(v2) + 1):
    v5 = v1[v4:v4 + len(v2)]
    v6 = 0
    for v7 in range(len(v2)):
        if v2[v7] != v5[v7]:
            v6 += 1
    v3.append(v6)
print(min(v3))
