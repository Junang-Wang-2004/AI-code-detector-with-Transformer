v1 = list(input())
v2, v3 = (0, len(v1) - 1)
v4 = 0
while v2 < v3:
    if v1[v2] == v1[v3]:
        v2 += 1
        v3 -= 1
    elif v1[v2] == 'x':
        v2 += 1
        v4 += 1
    elif v1[v3] == 'x':
        v3 -= 1
        v4 += 1
    else:
        print('-1')
        break
else:
    print(v4)
