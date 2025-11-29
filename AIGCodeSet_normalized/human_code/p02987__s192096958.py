v1 = input()
v2 = []
for v3 in range(len(v1)):
    v2.append(v1[v3])
v2.sort()
if v2[0] == v2[1] and v2[2] == v2[3] and (v2[1] != v2[2]):
    print('Yes')
else:
    print('No')
