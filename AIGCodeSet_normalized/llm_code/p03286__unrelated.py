v1 = int(input())
if v1 == 0:
    print(0)
    exit()
v2 = ''
while v1 != 0:
    if v1 % 2 == 1:
        v2 += '1'
        v1 -= 1
    else:
        v2 += '0'
    v1 //= -2
print(v2[::-1])
