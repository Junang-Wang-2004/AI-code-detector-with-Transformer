v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = input()
    v5 = [0, 0]
    if v4 != '':
        v6, v7 = (0, 0)
        for v8 in v4:
            if v8 == '(':
                v6 += 1
            elif v6 > 0:
                v6 -= 1
            else:
                v7 += 1
        if v6 != v7:
            print('No')
            exit()
        v5 = [v6, v7]
    v2.append(v5)
v9, v10 = (0, 0)
for v5 in v2:
    v9 += v5[0]
    v10 += v5[1]
if v9 != v10:
    print('No')
else:
    v11 = []
    for v5 in v2:
        for v12 in range(v5[0]):
            v11.append('(')
        for v12 in range(v5[1]):
            if v11:
                v11.pop()
            else:
                print('No')
                exit()
    if v11:
        print('No')
    else:
        print('Yes')
