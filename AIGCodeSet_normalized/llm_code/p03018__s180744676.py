v1 = input()
v1 = v1.replace('BC', 'D')
v2 = 0
v3 = 0
v4 = 0
for v5 in v1[::-1]:
    if v5 == 'D':
        v3 += 1
    elif v5 == 'A':
        v4 += v2 * v3
        v2 += 1
    else:
        v2 = 0
        v3 = 0
v4 += v2 * v3
print(v4)
