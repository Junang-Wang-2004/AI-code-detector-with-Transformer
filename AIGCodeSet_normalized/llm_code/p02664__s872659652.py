v1 = input()
v2 = [i for v3 in v1]
if v2[0] == '?':
    v2[0] = 'D'
for v3 in range(1, len(t) - 1):
    if v2[v3] == '?':
        if v2[v3 - 1] == 'D' and v2[v3 + 1] == 'D':
            v2[v3] = 'P'
        elif v2[v3 - 1] == 'D' and v2[v3 + 1] == '?':
            v2[v3] = 'P'
        else:
            v2[v3] = 'D'
if v2[-1] == '?':
    v2[-1] = 'D'
print(''.join(v2))
