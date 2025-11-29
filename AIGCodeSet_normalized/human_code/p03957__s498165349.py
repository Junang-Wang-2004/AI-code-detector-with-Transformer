v1 = input()
v2 = v1.find('C')
v3 = v1[v2:].find('F') + v2
if v2 < 0 or v3 < 0:
    print('No')
    exit()
print('Yes' if v3 - v2 > 0 else 'No')
