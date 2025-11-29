v1 = input()
v2 = []
for v3 in v1:
    if v3 not in v2:
        v2.append(v3)
if len(v2) == 2:
    print('Yes')
else:
    print('No')
