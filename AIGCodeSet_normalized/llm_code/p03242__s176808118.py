v1 = input()
v2 = ''
for v3 in range(len(v1)):
    if v1[v3] == '9':
        v2 += '1'
    else:
        v2 += '9'
print(v2)
