v1 = 'qwertyuiopasdfghjklzxcvbnm'
v2 = sorted(list(v1))
v3 = list(set(input()))
for v4 in v2:
    if not v4 in v3:
        print(v4)
        break
else:
    print('None')
