v1 = input()
v2 = 'keyence'
for v3 in range(len(v2)):
    if v1.find(v2[v3:]) > v1.find(v2[:v3]) >= 0:
        print('YES')
        exit()
print('NO')
