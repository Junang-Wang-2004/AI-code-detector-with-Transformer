v1 = input()
if v1.count('N') == 0 and v1.count('S') == 0:
    if v1.count('W') >= 1 and v1.count('E') >= 1:
        print('Yes')
        exit()
if v1.count('W') == 0 and v1.count('E') == 0:
    if v1.count('N') >= 1 and v1.count('S') >= 1:
        print('Yes')
        exit()
if v1.count('W') >= 1 and v1.count('E') >= 1 and (v1.count('N') >= 1) and (v1.count('S') >= 1):
    print('Yes')
    exit()
print('No')
