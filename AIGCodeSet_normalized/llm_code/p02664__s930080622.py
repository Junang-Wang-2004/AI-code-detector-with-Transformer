v1 = list(input())
for v2 in reversed(range(len(v1))):
    if v1[v2] == '?':
        if v2 == len(v1) - 1:
            v1[v2] = 'D'
        elif v1[v2 + 1] == 'D':
            v1[v2] = 'P'
        else:
            v1[v2] = 'D'
    else:
        continue
print(''.join(v1))
