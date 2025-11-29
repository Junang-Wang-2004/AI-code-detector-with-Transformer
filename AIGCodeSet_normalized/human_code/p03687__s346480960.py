v1 = input()
v2 = list(set(v1))
v3 = []
for v4 in range(len(v2)):
    v5 = list(v1.split(v2[v4]))
    v6 = []
    for v7 in range(len(v5)):
        v6.append(len(v5[v7]))
    v3.append(max(v6))
print(min(v3))
