v1 = input()
v2 = v1.find('C')
if v2 != -1:
    v3 = v1[v2:].find('F')
    if v3 != -1 and v3 > 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
