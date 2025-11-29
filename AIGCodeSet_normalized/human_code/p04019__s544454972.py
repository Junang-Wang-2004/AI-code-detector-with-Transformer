v1 = input()
v2 = set()
for v3 in v1:
    v2.add(v3)
if len(v2) == 4:
    print('Yes')
elif len(v2) == 2 and 'N' in v2 and ('S' in v2):
    print('Yes')
elif len(v2) == 2 and 'E' in v2 and ('W' in v2):
    print('Yes')
else:
    print('No')
