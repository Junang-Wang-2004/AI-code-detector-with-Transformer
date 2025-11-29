v1 = int(input())
v2 = input()
v3 = input()
v4 = 0
v5 = []
while v4 < v1:
    if v2[v4] == v3[v4]:
        v5.append('C')
    else:
        v5.append('R')
        v4 += 1
    v4 += 1
v6 = 3 if v5[0] == 'C' else 6
for v4 in range(1, len(v5)):
    if v5[v4 - 1] == 'C':
        if v5[v4] == 'C':
            v6 *= 2
        else:
            v6 *= 2
    elif v5[v4] == 'C':
        v6 *= 1
    else:
        v6 *= 3
    v6 %= 10 ** 9 + 7
print(v6)
