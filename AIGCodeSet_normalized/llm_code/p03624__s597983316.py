import string
v1 = list(input())
v1 = list(set(v1))
v1.sort()
v2 = ''
v3 = list(string.ascii_lowercase)
for v4 in range(len(v3)):
    if v3[v4] not in v1:
        v2 = v3[v4]
        break
if v2 == '':
    v2 = 'None'
print(v2)
