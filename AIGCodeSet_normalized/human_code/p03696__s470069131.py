v1 = int(input())
v2 = list(input())
v3 = []
v4 = 0
for v5 in v2:
    if v5 == '(':
        v4 += 1
        v3.append('(')
    elif v4 == 0:
        v3.insert(0, '(')
        v3.append(')')
    else:
        v4 -= 1
        v3.append(')')
for v5 in range(v4):
    v3.append(')')
print(*v3, sep='')
