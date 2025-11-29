v1 = input()
v2 = 'NO'
for v3 in range(len(v1) + 1):
    for v4 in range(v3, len(v1) + 1):
        v5 = v1[:v3]
        v6 = v1[v4:]
        if v5 + v6 == 'keyence':
            v2 = 'YES'
print(v2)
