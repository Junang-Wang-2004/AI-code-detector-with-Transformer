v1 = str(input())
v2 = ''
for v3 in range(len(v1)):
    if v1[v3] == '1':
        v2 += '9'
    else:
        v2 += '1'
print(v2)
