v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(input())
v4 = 0
for v5 in v2:
    for v6 in v5:
        if v6 == '(':
            v4 += 1
        else:
            v4 -= 1
        if v4 < 0:
            print('No')
            exit()
if v4 == 0:
    print('Yes')
else:
    print('No')
