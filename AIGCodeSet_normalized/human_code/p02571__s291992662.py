v1 = input()
v2 = input()
v3 = 0
for v4 in range(len(v1) - len(v2) + 1):
    v5 = v1[v4:v4 + len(v2)]
    v6 = 0
    for v7, v8 in zip(v5, v2):
        if v7 == v8:
            v6 += 1
    v3 = max(v6, v3)
print(len(v2) - v3)
