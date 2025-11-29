v1 = input()
v2 = input()
v3 = len(v2)
for v4 in range(0, len(v1) - len(v2) + 1):
    v5 = 0
    for v6 in range(len(v2)):
        if v1[v6 + v4] != v2[v6]:
            v5 += 1
    if v5 < v3:
        v3 = v5
print(v3)
