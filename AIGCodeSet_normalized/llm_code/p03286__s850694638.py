v1 = int(input())
str = ''
while v1 != 0:
    if v1 % 2:
        v1 -= 1
        v1 //= -2
        str += '1'
    else:
        v1 //= -2
        str += '0'
if str == '':
    print(0)
else:
    print(str[::-1])
