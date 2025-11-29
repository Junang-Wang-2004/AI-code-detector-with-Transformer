v1 = input()
if 'C' in v1:
    v2 = v1.index('C')
    if 'F' in v1[v2:]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
