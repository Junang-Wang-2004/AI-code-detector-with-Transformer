v1 = int(input())
v2 = ['a']
v3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
if v1 == 1:
    print('a')
    exit()
else:
    for v4 in range(v1 - 1):
        v5 = []
        for v6 in range(len(v2)):
            for v7 in range(len(set(v2[v6])) + 1):
                v5.append(v2[v6] + v3[v7])
        v2 = v5
for v4 in range(len(v5)):
    print(v5[v4])
