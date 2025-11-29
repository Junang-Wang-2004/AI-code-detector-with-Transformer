v1 = int(input())
v2 = ''
while v1 != 0:
    if v1 % 2 != 0:
        v1 -= 1
        v2 = '1' + v2
    else:
        v2 = '0' + v2
    v1 /= -2
if v2 == '':
    v2 = '0'
print(v2)
