v1 = input().split()
v2 = [input().split() for v3 in range(int(v1[1]))]
v4 = set()
v5 = set()
for v6 in v2:
    if v6[0] == '1':
        v4.add(v6[1])
    if v6[1] == v1[0]:
        v5.add(v6[0])
if v4 & v5:
    print('POSSIBLE')
else:
    print('INPOSSIBLE')
