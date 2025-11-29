str = input()
v1 = str.split(' ')
v2 = int(v1[0])
v3 = int(v1[1])
v4 = int(v1[2])
v5 = int(v1[3])
v6 = int(v1[4])
v7 = v2 * 60 + v3
v8 = v4 * 60 + v5
v9 = v8 - v7 - v6
if v9 >= 0:
    print(v9)
else:
    print('0')
