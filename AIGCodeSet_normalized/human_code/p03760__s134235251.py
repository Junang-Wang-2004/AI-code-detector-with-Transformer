v1 = input()
v2 = input()
v3 = len(v1)
v4 = len(v2)
v5 = ''
if v3 > v4:
    for v6 in range(v3):
        if v6 + 1 == v3:
            v5 += v1[v6]
        else:
            v5 += v1[v6]
            v5 += v2[v6]
else:
    for v6 in range(v4):
        v5 += v1[v6]
        v5 += v2[v6]
print(v5)
