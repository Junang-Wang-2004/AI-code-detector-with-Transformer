v1 = input()
v2 = 'abcdefghijklmnopqrstuvwxyz'
for v3 in v2:
    if v3 not in v1:
        print(v3)
        break
else:
    print('None')
