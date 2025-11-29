v1 = input()
v2 = list(v1)
for v3 in range(len(v2)):
    if v2[v3] == '?':
        if v3 > 0 and v2[v3 - 1] == 'P':
            v2[v3] = 'D'
        elif v3 < len(v2) - 1 and v2[v3 + 1] == 'D':
            v2[v3] = 'P'
        elif v3 > 0 and v2[v3 - 1] == 'D':
            v2[v3] = 'P'
        else:
            v2[v3] = 'D'
v4 = ''.join(v2)
print(v4)
