v1 = int(input())
v2 = []
v3 = v1 + 1 if v1 % 2 == 0 else v1
for v4 in range(1, v1 + 1):
    for v5 in range(v4 + 1, v1 + 1):
        if v4 + v5 == v3:
            continue
        v2.append('{} {}'.format(v4, v5))
print(len(v2))
print('\n'.join(v2))
