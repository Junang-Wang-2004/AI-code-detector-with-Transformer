v1 = input()
v2 = v1.split('/')
v3 = 'Heisei'
if int(v2[1]) > 4 or (int(v2[1]) == 4 and int(v2[2]) > 30):
    v3 = 'TBD'
print(v3)
