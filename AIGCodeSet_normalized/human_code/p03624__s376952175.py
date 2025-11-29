v1 = sorted(input())
v2 = 'abcdefghijklmnopqrstuvwxyz'
for v3 in range(26):
    if not v2[v3] in v1:
        print(v2[v3])
        break
    if v2[v3] == 'z':
        print('None')
