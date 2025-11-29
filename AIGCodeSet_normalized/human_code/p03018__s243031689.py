v1 = input().replace('BC', 'D') + 'E'
v2 = []
v3 = ''
for v4 in v1:
    if v4 == 'A' or v4 == 'D':
        v3 += v4
    else:
        v2.append(v3)
        v3 = ''
v5 = 0
for v4 in v2:
    v6 = 0
    for v7 in v4:
        if v7 == 'A':
            v6 += 1
        else:
            v5 += v6
print(v5)
