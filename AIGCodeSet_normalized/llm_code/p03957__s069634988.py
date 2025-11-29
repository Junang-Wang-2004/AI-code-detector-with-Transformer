v1 = input()
v2 = False
v3 = False
for v4 in v1:
    if v4 == 'C':
        v2 = True
    if v4 == 'F':
        v3 = True
    if v2 == True and v3 == True:
        print('Yes')
        break
if not (v2 == True and v3 == True):
    print('No')
