from collections import Counter
v1 = input()
v2 = input()
for v3 in list(v1):
    if v3 in list(v2):
        v1 = list(v1)
        v2 = list(v2)
        v4 = v1.index(v3)
        del v1[v4]
        del v2[v4]
        v1 = ''.join(v1)
        v2 = ''.join(v2)
v5 = Counter(v1)
v6 = []
v7 = Counter(v2)
v8 = []
for v9, v10 in list(v5.items()):
    for v11, v12 in list(v7.items()):
        if v10 == v12:
            v6.append(v9)
            v8.append(v11)
            del v5[v9]
            del v7[v11]
            break
if len(v1) == len(v6):
    print('Yes')
else:
    print('No')
