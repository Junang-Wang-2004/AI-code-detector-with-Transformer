v1 = input()
v2 = ''
for v3 in range(len(v1)):
    if v1[v3] == '?':
        if v3 != len(v1) - 1:
            if v1[v3 + 1] == 'D':
                v2 += 'P'
            else:
                v2 += 'D'
        else:
            v2 += 'D'
    else:
        v2 += v1[v3]
print(v2)
