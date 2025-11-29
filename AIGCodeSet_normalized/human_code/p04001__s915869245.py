v1 = input()
v2 = len(v1) - 1
v3 = 0
for v4 in range(1 << v2):
    v5 = 0
    for v6 in range(v2):
        if v4 >> v6 & 1 == 1:
            v3 += int(''.join(v1[v5:v6 + 1]))
            v5 = v6 + 1
    v3 += int(''.join(v1[v5:]))
print(v3)
