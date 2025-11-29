v1 = int(input())
v2 = str(v1)
v3 = ''
for v4 in v2:
    if v4 == '1':
        v3 += '9'
    elif v4 == '9':
        v3 += '1'
    else:
        v3 += v4
print(int(v3))
