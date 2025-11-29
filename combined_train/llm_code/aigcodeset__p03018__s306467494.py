v1 = list(input())
v2 = 0
v3 = 0
v4 = 0
v5 = []
while v2 != len(v1) - 2:
    try:
        if v1[v2] == 'A' and v1[v2 + 1] == 'B' and (v1[v2 + 2] == 'C'):
            v5.append(1)
            v2 = v2 + 3
        elif v1[v2] == 'B' and v1[v2 + 1] == 'C':
            v5.append(2)
            v2 = v2 + 2
        elif v1[v2] == 'A':
            v5.append(3)
            v2 = v2 + 1
        else:
            v5.append(0)
            v2 = v2 + 1
    except:
        break
v4 = 0
v2 = 0
v6 = 0
v7 = 0
v8 = 0
while v2 != len(v5):
    if v5[v2] == 1:
        v6 = v6 + 1
        v4 = v4 + v6
        v4 = v4 + v8
        if v7 != 0:
            v8 = 0
        v7 = 0
    elif v5[v2] == 2:
        if v6 >= 1:
            v7 = v7
            v4 = v4 + v6 + v8
    elif v5[v2] == 3:
        v8 = v8 + 1
    else:
        v6 = 0
        v7 = 0
        v8 = 0
    v2 = v2 + 1
print(v4)
