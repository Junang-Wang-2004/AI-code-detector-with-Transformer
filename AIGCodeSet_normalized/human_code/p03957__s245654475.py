v1 = input()
if 'C' in v1:
    v2 = v1.find('C')
    if 'F' in v1[v2:]:
        print('Yes')
        exit(0)
print('No')
