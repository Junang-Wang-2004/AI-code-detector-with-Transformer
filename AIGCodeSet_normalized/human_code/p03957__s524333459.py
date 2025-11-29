v1 = input()
v2 = 0
for v3 in range(len(v1)):
    if v1[v3] == 'C':
        v2 = 1
    if v1[v3] == 'F' and v2:
        print('Yes')
        exit()
print('No')
