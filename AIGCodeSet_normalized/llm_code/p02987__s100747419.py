v1 = input()
v2 = 1
v3 = 0
for v4 in range(4):
    if v1[v4] == v1[0]:
        v2 += 1
    else:
        v3 += 1
if v3 == 2 and v2 == 2:
    print('Yes')
else:
    print('No')
