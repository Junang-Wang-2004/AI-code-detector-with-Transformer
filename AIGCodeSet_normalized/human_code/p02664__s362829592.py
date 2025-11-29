v1 = list(input())
for v2 in range(len(v1)):
    if v1[v2] == '?':
        v1[v2] = 'D'
print(*v1, sep='')
