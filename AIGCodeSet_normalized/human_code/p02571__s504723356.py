v1 = input()
v2 = input()
v3 = []
for v4 in range(len(v1) - len(v2) + 1):
    v5 = 0
    for v6 in range(len(v2)):
        if v1[v4 + v6] != v2[v6]:
            v5 += 1
    v3.append(v5)
print(min(v3))
