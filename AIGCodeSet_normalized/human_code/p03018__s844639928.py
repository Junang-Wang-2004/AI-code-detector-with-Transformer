v1 = input().replace('BC', 'D')
v2 = 0
v3 = 0
for v4 in range(len(v1)):
    if v1[v4] == 'A':
        v3 += 1
    elif v1[v4] == 'D':
        v2 += v3
    else:
        v3 = 0
print(v2)
