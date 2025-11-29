v1 = int(input())
if v1 == 0:
    print(0)
    exit()
v2 = ''
while v1 != 0:
    if v1 % -2 < 0:
        v3 = v1 % -2 + 2
        v1 = v1 // -2 + 1
    else:
        v3 = v1 % -2
        v1 = v1 // -2
    v2 += str(v3)
print(int(v2[::-1]))
