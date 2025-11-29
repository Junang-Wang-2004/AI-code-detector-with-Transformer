v1 = int(input())
if v1 == 0:
    print(0)
    exit()
v2 = []
v3 = v1
while v3 != 1:
    if v3 % 2 == 0:
        v2.append('0')
    else:
        v2.append('1')
        v3 -= 1
    v3 /= -2
v2.append('1')
v4 = ''.join(v2[::-1])
print(v4)
