v1, v2, v3 = list(map(int, input().split()))
v4 = str(input())
v5 = 0
v6 = 0
for v7 in v4:
    v8 = ''
    if v5 + v6 >= v2 + v3:
        v8 = 'No'
    elif v7 == 'a':
        v5 += 1
        v8 = 'Yes'
    elif v7 == 'b':
        v8 = 'Yes'
        if v6 >= v3:
            v8 = 'No'
        else:
            v6 += 1
    else:
        v8 = 'No'
    print(v8)
