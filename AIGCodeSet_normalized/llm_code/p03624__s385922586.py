v1 = input()
v2 = 'abcdefghijklmnopqrstuvwxyz'
v3 = set(v1)
v3 = sorted(v3)
if all((c in v3 for v4 in v2)):
    print('None')
else:
    for v5 in range(len(v1)):
        if v3[v5] != v2[v5]:
            print(v2[v5])
            break
