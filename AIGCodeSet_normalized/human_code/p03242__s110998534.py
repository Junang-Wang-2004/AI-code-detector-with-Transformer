v1 = list(input())
for v2 in range(3):
    if v1[v2] == '1':
        v1[v2] = '9'
    else:
        v1[v2] = '1'
print(''.join(v1))
