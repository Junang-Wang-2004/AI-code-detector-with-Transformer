v1 = input()
v2 = input()
v3 = len(v1)
v4 = len(v2)
v5 = v4
for v6 in range(0, v3 - v4 + 1):
    v7 = 0
    for v8 in range(v4):
        if v1[v6 + v8] != v2[v8]:
            v7 += 1
    v5 = min(v5, v7)
print(v5)
