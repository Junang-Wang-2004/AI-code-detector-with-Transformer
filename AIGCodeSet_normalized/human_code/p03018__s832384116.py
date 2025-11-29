v1 = input().replace('BC', 'D')
v2 = 0
v3 = 0
for v4 in v1:
    if v4 == 'A':
        v2 += 1
    elif v4 == 'D':
        v3 += v2
    else:
        v2 = 0
print(v3)
