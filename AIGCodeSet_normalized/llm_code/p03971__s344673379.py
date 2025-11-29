v1, v2, v3 = map(int, input().split())
v4 = list(input())
v5 = []
v6 = 0
v7 = 0
v8 = v2 + v3
for v9 in v4:
    if v9 == 'c':
        v5.append('No')
    elif v9 == 'a' and v6 < v8:
        v5.append('Yes')
        v6 += 1
    elif v9 == 'b' and v6 < v8 and (v7 < v3):
        v5.append('Yes')
        v6 += 1
        v7 += 1
    else:
        v5.append('No')
print('\n'.join(v5))
