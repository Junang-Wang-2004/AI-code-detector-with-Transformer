v1 = input()
v2 = 'keyence'
v3 = 0
v4 = False
v5 = 0
for v6 in range(len(v1)):
    if v2[v5] == v1[v6]:
        if v4 == True:
            v4 = False
            v3 = v3 + 1
        v5 = v5 + 1
    else:
        v4 = True
print('YES' if v5 == len(v2) and v3 <= 1 else 'N0')
