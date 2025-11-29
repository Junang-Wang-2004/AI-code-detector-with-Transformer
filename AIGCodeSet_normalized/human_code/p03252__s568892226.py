v1 = list(input())
v2 = list(input())
v3 = {}
v4 = {}
for v5 in range(len(v1)):
    if v1[v5] in v3:
        if v3[v1[v5]] != v2[v5]:
            print('No')
            exit()
    else:
        v3[v1[v5]] = v2[v5]
    if v2[v5] in v4:
        if v4[v2[v5]] != v1[v5]:
            print('No')
            exit()
    else:
        v4[v2[v5]] = v1[v5]
print('Yes')
