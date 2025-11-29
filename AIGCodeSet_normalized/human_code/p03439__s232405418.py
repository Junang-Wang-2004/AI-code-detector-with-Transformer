v1 = int(input())
print(0)
v2 = input()
v3 = {}
if v2 == 'Vacant':
    exit(0)
elif v2 == 'Male':
    v3['Male'] = 1
    v3['Female'] = 2
else:
    v3['Male'] = 2
    v3['Female'] = 1
print(v1 - 2)
v2 = input()
if v2 == 'Vacant':
    exit(0)
elif v3[v2] == 2:
    print(v1 - 1)
    exit(0)
v4 = v1 - 2
v5 = 0
while v4 - v5 >= 2:
    v6 = (v4 + v5 + 1) // 2
    print(v6)
    v2 = input()
    if v2 == 'Vacant':
        exit(0)
    if (v6 + v3[v2]) % 2 == 1:
        v5 = v6
    else:
        v4 = v6
    v6 = (v4 + v5 + 1) // 2
print(v4)
v2 = input()
if v2 == 'Vacant':
    exit(0)
print(v5)
v2 = input()
if v2 == 'Vacant':
    exit(0)
