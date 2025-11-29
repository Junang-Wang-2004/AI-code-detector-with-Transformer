v1 = input()
v1 = list(v1)
v2 = 0
while v2 == 0:
    if 'N' in v1:
        if 'S' in v1:
            v2 += 1
        else:
            print('No')
            break
    if 'S' in v1:
        if 'N' in v1:
            v2 += 1
        else:
            print('No')
            break
    if 'E' in v1:
        if 'W' in v1:
            v2 += 1
        else:
            print('No')
            break
    if 'W' in v1:
        if 'E' in v1:
            v2 += 1
        else:
            print('No')
            break
else:
    print('Yes')
