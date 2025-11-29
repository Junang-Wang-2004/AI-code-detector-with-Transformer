v1, v2 = map(int, input().split())
v3, v4, v5 = map(int, input().split())
v6 = list(input())
v7 = []
v8 = 0
for v9 in range(v1):
    if v6[v9] == 'r':
        v7.append('p')
    elif v6[v9] == 's':
        v7.append('r')
    else:
        v7.append('s')
for v9 in range(v1):
    if v9 >= v2:
        if v7[v9] == v7[v9 - v2]:
            if v9 + v2 > v1:
                pass
            elif v7[v9 + v2] != v6[v9]:
                v7[v9] = v6[v9]
            elif v7[v9] != v3 and [v9 + v2] != v3:
                v7[v9] = v3
            elif v7[v9] != v4 and [v9 + v2] != v4:
                v7[v9] = v4
            elif v7[v9] != v5 and [v9 + v2] != v5:
                v7[v9] = v5
        elif v7[v9] == 'r':
            v8 += v3
        elif v7[v9] == 's':
            v8 += v4
        else:
            v8 += v5
    elif v7[v9] == 'r':
        v8 += v3
    elif v7[v9] == 's':
        v8 += v4
    else:
        v8 += v5
print(v8)
